resource "local_file" "pets" {
  filename = var.filename[count.index]
  content  = "MY DOG Prince ${random_pet.my_pet.id}"
  count    = length(var.filename)
}

resource "random_pet" "my_pet" {
  prefix    = var.prefix
  separator = var.separator
  length    = var.length

}

output "pets" {
  value     = local_file.pets
  sensitive = false
}

output "my_pet" {
  value     = random_pet.my_pet
  sensitive = false
}
