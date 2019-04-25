from bs4 import BeautifulSoup
import requests
#Curso UDEMY web scraping
url = 'https://listado.mercadolibre.cl/mitos-y-leyendas#D[A:mitos%20y%20leyendas]'
page_num = 1
while True:
    #------- Pasos necesarios para realizar scraping -------#
    print('--------- pagina ',page_num,' --------------')
    response = requests.get(url)             # Hace peticiones a la url
    data = response.text                     # Obtiene todo el codigo de la página en un solo texto.  
    soup = BeautifulSoup(data,'html.parser') # Pasa el texto a codigo html, para posteriores consultas.
    #------- ------- ------- ------- ------- ------- -------#
    items = soup.find_all('li',{'class':'results-item highlighted article stack'})
    for item in items:
        title = item.find('span',{'class':'main-title'}).text
        price = item.find('span',{'class':'price__fraction'}).text
        link = item.find('a',{'class':'item__info-title'}).get('href')

        item_response = requests.get(link)
        item_data = item_response.text
        item_soup = BeautifulSoup(item_data,'html.parser')
        
        #item_description_tag = item_soup.find('div',{'class':'item-description__content'})
        #item_description = item_description_tag.text if item_description_tag else 'NN'
        
        #item_char_tag = item_soup.find('div',{'class':'specs-wrapper'})
        #item_char = item_char_tag.text if item_char_tag else 'NN'
        print('Titulo: ',title, '\nPrecio: ',price)        
    link_next_page = soup.find('a',{'class':'andes-pagination__link prefetch'})
    if link_next_page.get('href'):
        url = link_next_page.get('href')
        print(url)
        page_num= 1+page_num
    else:  
        break
print('numero de paginas: ',page_num)