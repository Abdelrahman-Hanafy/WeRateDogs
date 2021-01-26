import requests

url = "https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv"
page = requests.get(url)
#print(page.text)
with open("image_predictions.tsv","w") as f:
    f.write(page.text)

