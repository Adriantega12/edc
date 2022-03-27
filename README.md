# EDC

Short script to quickly process and classify monthly expenses. Copy and paste concepts from an EDC with however you wanna clasify them, in the following format:

```
# <concept name 1>
<expense 1>
<expense 2>
...
<expense n>
# <concept name 2>
<expense 1>
<expense 2>
...
<expense n>
```

Most EDCs' concepts include the expense in the format of `<date> <concept short description> $ <expense total> <bank's given class>`, script will use the space between "$" and the expense total to get it so it's important that it remains there, for example:

```
# Transportation
28/02/2022 STP UBER PENDING $ 145.19 TRANSPORTE
# Food
28/02/2022 DLOCAL*DIDI FOOD $ 98.50 TRANSPORTE
```

Final output will be:

```
Transportation: $145.19
Food: $98.50
------------
GRAND TOTAL: $243.69
```