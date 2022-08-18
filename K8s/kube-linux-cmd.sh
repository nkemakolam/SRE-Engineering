# taking count of the namespace 
# not that when you do wc -l it count from the header of the line
# to remove the header being counted we use the tail -n +2

kubectl get ns | tail -n +2 |wc -l

kubectl get ns|grep sand| tail -n +2 | wc -l

kubectl exec -it pod_name -- /bin/bash

**CPU**
cd /sys/fs/cgroup/cpu
cat cpuacct.usage

**Memeory*
cd /sys/fs/cgroup/memory

cat memory.usage_in_bytes