import requests

print('Hello welcome to IpChecker free tool')
print('\nWhom do you want to check ?\n')



def mySelf(ip):
    
    all_par = requests.get(f'https://get.geojs.io/v1/ip/geo/{ip}.json').json()

    print(
        f'''
            accuracy: {all_par.get('accuracy')}\n
            country: {all_par.get('country')}\n
            area_code: {all_par.get('area_code')}\n
            latitude: {all_par.get('latitude')}\n
            longitude: {all_par.get('longitude')}\n
            ip: {all_par.get('ip')}\n
            organization: {all_par.get('organization')}
        '''
    )
    
    print('\nCreated by GitHub: @Dilmuhammad06')
    


ans = int(input('Myself (1) | Other person (2):\n'))

if ans == 1:
    
    MY_IP = requests.get('https://get.geojs.io/v1/ip.json').json().get('ip')
    
    mySelf(MY_IP)
    
elif ans ==2:
    ip = input('Input ip like \'192.168.1.1\':\n')
    
    mySelf(ip)
    
else:
    print('Out of order ERROR')

