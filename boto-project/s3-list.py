'''
region            bucket_details
'us-east-1'        1
                   2

'''
import pandas as pd
inp_data = {'us-east-1': ['1','2','3','4'], 'us-west-1': ['4','5'],
        'ap-south-1': ['7']}

region_lst = []
bucket_name_lst = []
data = {'region': region_lst, 'bucket_names':bucket_name_lst}

for k,v in inp_data.items():
    region_lst.append(k)
    bucket_name_lst.append(v[0])
    for i in v[1:]:
        region_lst.append(' ')
        bucket_name_lst.append(i)
df = pd.DataFrame(data)
df.to_excel('output.xlsx', encoding='utf-8', index=False)

obj = pd.read_json('exp.json', orient='columns')
obj = obj.reset_index()
obj = obj.explode("inp_data")
obj['index'] = obj['index'].mask(obj['index'].duplicated(), "")
obj.to_csv('out.csv',index=False)


import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='143.244.141.41',
                   username='heartfulcoding',password='heart@123')

cmd_str = 'ifconfig'

stdin, stdout, stderr = ssh_client.exec_command(cmd_str)
output = stdout.read().decode('utf-8')
# print(output)