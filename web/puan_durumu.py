from bs4 import BeautifulSoup
import requests


class PuanDurum(object):
    @staticmethod
    def puan_durumu():
        url = 'http://fikstur.kutahyaaskf.org.tr/lmo.php?todo=&file=GED%DDZ-%20EMET-%20H%DDSARCIK%20.%20AMAT.l98'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.findAll("table", class_="lmoInner")
        puan_tablosu = tables[1]

        pre_result =[]
        result=[]

        for row in puan_tablosu.findAll("tr"):
            cells = row.findAll("td")
            if len(cells) == 18:
                list=[]
                for data in cells:
                    for val in data:
                        try:
                            list.append(val.string.strip())
                        except TypeError:
                            pass
                        except AttributeError:
                            pass


                pre_result.append(list)


        for sublist in pre_result:
            temiz_liste = [x for x in sublist if x is not None and x.strip().replace(':', '')]
            temiz_liste.pop(6)
            temiz_liste.pop(6)
            result.append(temiz_liste)

        return result