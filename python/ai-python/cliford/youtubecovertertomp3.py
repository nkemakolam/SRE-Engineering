import os
import pytube
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

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

def generate_summary(text, num_sentences=5):
    sentences = text.split('.')
    
    stop_words = stopwords.words('english')
    
    similarity_matrix = build_similarity_matrix(sentences, stop_words)
    
    # PageRank algorithm to rank sentences
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)
    
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    # Get the top N sentences as the summary
    summary = [ranked_sentences[i][1] for i in range(num_sentences)]
    
    return ' '.join(summary)

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=WVNvoiA_ktw"
    output_path = "./"
    
    # Download the YouTube video as an audio file
    audio_file = download_youtube_video(youtube_url, output_path)
    
    # Fetch the transcript of the video
    video_transcript = fetch_youtube_transcript(youtube_url)
    
    # Generate a summary from the video transcript
    summary = generate_summary(video_transcript)
    
    # Save the summary to a text file
    with open("video_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    
    print("Summary generated and saved as 'video_summary.pdf'.")
    
    

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

