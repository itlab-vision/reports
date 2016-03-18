##Результаты сегментации __val__ датасета для обученной нами модели largeFOV после crf:
Accuracy for each class (intersection/union measure)
```
      background: 93.168%
       aeroplane: 85.908%
         bicycle: 35.281%
            bird: 87.322%
            boat: 69.722%
          bottle: 74.262%
             bus: 87.573%
             car: 82.952%
             cat: 86.548%
           chair: 45.222%
             cow: 79.658%
     diningtable: 59.474%
             dog: 82.678%
           horse: 80.665%
       motorbike: 79.027%
          person: 81.400%
     pottedplant: 59.845%
           sheep: 82.783%
            sofa: 52.021%
           train: 81.957%
       tvmonitor: 65.882%
-------------------------
Average accuracy: 73.969%
```


##Результаты deeplab_largeFOV после crf на val:
Accuracy for each class (intersection/union measure)
```
      background: 93.977%
       aeroplane: 87.282%
         bicycle: 38.160%
            bird: 88.285%
            boat: 73.817%
          bottle: 78.853%
             bus: 90.984%
             car: 84.549%
             cat: 89.581%
           chair: 42.027%
             cow: 87.134%
     diningtable: 65.741%
             dog: 87.891%
           horse: 83.470%
       motorbike: 80.470%
          person: 83.793%
     pottedplant: 65.909%
           sheep: 89.536%
            sofa: 65.953%
           train: 86.193%
       tvmonitor: 66.179%
-------------------------
Average accuracy: 77.609%
```
На тестовых данных их результаты падают на 7% как видно из [таблицы](http://host.robots.ox.ac.uk:8080/leaderboard/displaylb.php?cls=mean&challengeid=11&compid=6&submid=4581).


##Результаты deeplab_MSc_CRF_largeFOV на val:
Accuracy for each class (intersection/union measure)
```
      background: 94.797%
       aeroplane: 89.681%
         bicycle: 61.726%
            bird: 89.355%
            boat: 79.238%
          bottle: 79.276%
             bus: 90.856%
             car: 85.748%
             cat: 89.883%
           chair: 43.446%
             cow: 88.147%
     diningtable: 65.292%
             dog: 89.012%
           horse: 84.817%
       motorbike: 81.897%
          person: 85.012%
     pottedplant: 68.625%
           sheep: 90.930%
            sofa: 66.651%
           train: 86.722%
       tvmonitor: 66.367%
-------------------------
Average accuracy: 80.350%
```

##Результаты нашей MSc_CRF_largeFOV на val:
Accuracy for each class (intersection/union measure)
```
      background: 93.446%
       aeroplane: 87.810%
         bicycle: 37.295%
            bird: 87.934%
            boat: 70.576%
          bottle: 77.543%
             bus: 90.966%
             car: 83.090%
             cat: 87.331%
           chair: 39.676%
             cow: 86.184%
     diningtable: 60.957%
             dog: 85.646%
           horse: 82.628%
       motorbike: 78.506%
          person: 82.878%
     pottedplant: 60.192%
           sheep: 88.430%
            sofa: 54.002%
           train: 84.249%
       tvmonitor: 64.986%
-------------------------
Average accuracy: 75.444%
```
