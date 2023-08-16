# create ssh key for inter server copy
ssh-keygen -t ed25519 
# cat the ssh public key
cat /home/nkemakolam/.ssh/id_ed25519.pub
# decrypt the gpg backup from the download from storage using the key from the pmx-psql-backup-key key in the production ley vault
gpg --decrypt romania-prod-20221101003934.pg_dump.gpg > romania-prod.dump

# get you ip andress for white listing for shh
ifconfig or 
curl https://ipinfo.io
# ssh to the server to confirm connection
ssh jozian@13.80.125.224
#use scp to copy from your server to the ssh server
scp ./romania-prod.dump jozian@13.80.125.224:~/romania-prod.dump
create the user [user_demo_romania]  and role [ pmxprdpsqladmin] before running the command below to restore use pg_restore for the restore
pg_restore -U user_demo_romania  -d Romania -1 romania-prod.dump

ref
https://stackoverflow.com/questions/2732474/restore-a-postgres-backup-file-using-the-command-line