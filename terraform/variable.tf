variable "filename" {
  default = ["./terraform/bird.txt",
    "./terraform/dog.txt",
    "./terraform/cat.txt"
  ]
}
variable "content" {
  default = "I love my docg prince"
}
variable "prefix" {
  default = "Mrs"
}
variable "separator" {
  default = "."
}
variable "length" {
  default = "2"
}
