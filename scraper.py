import requests
from bs4 import BeautifulSoup

def extracting_image(url, header):
    
    page = requests.get(url, headers=header)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "lxml")
        links = soup.find_all("a")
        for link in links:
            print(link.text)



def main():
    
    url = "https://www.google.com/search?q=hacker+pics&tbm=isch&ved=2ahUKEwiOlOvVnKfoAhUS_xoKHS4dBVYQ2-cCegQIABAA&oq=hacker+pics&gs_l=img.3..0j0i67j0l8.533240.534133..534139...0.0..0.258.1894.2-8......0....1..gws-wiz-img.S3MBUq17BMQ&ei=dsFzXo4Bkv5rrrqUsAU&bih=625&biw=1366&rlz=1C1CHBD_enPK891PK891"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
    extracting_image(url, header)
    
    
    
if __name__ == "__main__":
    main()
    