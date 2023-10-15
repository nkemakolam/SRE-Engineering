import os
import pytube
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def download_youtube_video(youtube_url, output_path):
    yt = pytube.YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=output_path)
    return stream.default_filename

def fetch_youtube_transcript(youtube_url):
    video_id = youtube_url.split("v=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ' '.join([entry['text'] for entry in transcript])
    return text

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
    
    sent1 = [word.lower() for word in sent1]
    sent2 = [word.lower() for word in sent2]
    
    all_words = list(set(sent1 + sent2))
    
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stop_words)
    
    return similarity_matrix

# def generate_summary(text, num_sentences=5):
    sentences = text.split('.')
    
    stop_words = stopwords.words('english')
    
    similarity_matrix = build_similarity_matrix(sentences, stop_words)
    
    # PageRank algorithm to rank sentences
    nx_graph = nx.from_numpy_array(similarity_matrix)
    try:
        scores = nx.pagerank(nx_graph)
    except ZeroDivisionError as e:
        print(f"Error calculating similarity: {e}")
        scores = {}
    
    
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    # Get the top N sentences as the summary
    summary = [ranked_sentences[i][1] for i in range(num_sentences)]
    
    return ' '.join(summary)

# this function helps to handle long videos 

def generate_summary(text, num_sentences=5, segment_size=500):
    sentences = text.split('.')
    
    stop_words = stopwords.words('english')
    
    # Process the transcript in segments
    segment_summaries = []
    for i in range(0, len(sentences), segment_size):
        segment = sentences[i:i + segment_size]
        if len(segment) == 0:
            continue
        
        similarity_matrix = build_similarity_matrix(segment, stop_words)
        
        
        
        # PageRank algorithm to rank sentences within the segment
        nx_graph = nx.from_numpy_array(similarity_matrix)
        
        #nx.seterr(invalid='ignore')
        try:
          
            scores = nx.pagerank(nx_graph)
        except ZeroDivisionError as e:
            print(f"Error calculating similarity: {e}")
            scores = {}
        
        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(segment)), reverse=True)
        
        # Get the top N sentences as the summary for this segment
        segment_summary = [ranked_sentences[i][1] for i in range(num_sentences)]
        segment_summaries.extend(segment_summary)
    
    # Combine segment summaries to get the final summary
    return ' '.join(segment_summaries)

def save_summary_to_pdf_and_txt(text, pdf_filename, txt_filename):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    story = []
    
    # Add a title to the PDF
    title = Paragraph("Video Summary", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))
    
    # Generate summary with bullet points
    summary = text.split('.')
    bullet_points = ListFlowable(
        [Paragraph(sentence.strip(), styles['Normal']) for sentence in summary if sentence.strip()],
        bulletFontName='Helvetica',
        bulletFontSize=10,
        bulletIndent=20,
        bulletColor=colors.black
    )
    story.append(bullet_points)
    
    # Save the PDF
    doc.build(story)
    
    # Save the plain text summary
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=zGDTt9Q3vyM&t=10s"
    output_path = "./"
    
   
    # https://www.youtube.com/watch?v=zGDTt9Q3vyM&t=10s bitcoin
    # https://www.youtube.com/watch?v=WVNvoiA_ktw
    
    # Download the YouTube video as an audio file
    audio_file = download_youtube_video(youtube_url, output_path)
    
    # Fetch the transcript of the video
    video_transcript = fetch_youtube_transcript(youtube_url)
    
    # Generate a summary from the video transcript
    summary = generate_summary(video_transcript)
    
    # Save the summary to PDF and plaintext
    pdf_filename = "video_summary.pdf"
    txt_filename = "video_summary.txt"
    save_summary_to_pdf_and_txt(summary, pdf_filename, txt_filename)
    
    print("Summary generated and saved as 'video_summary.pdf' and 'video_summary.txt'.")


## How to set up the package  for this code 
# pip3 install pytube==11.0.1
# pip3 -m install youtube-transcript-api==0.4.1
# pip3 -m install nltk==3.6.3
# pip3 -m install numpy==1.21.2
# pip3 -m install networkx==2.6.3
# pip3 -m install nltk
# python -m pip install reportlab

# troublshooting no m,odule package use this command
# python --version
# pip show pytube
# pip cache purge
# pip install pytube



## after installation then go to 
#python 
#import nltk
# nltk.download('stopwords')

