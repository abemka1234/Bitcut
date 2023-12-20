# Bitcut
### Description
This is tool,that generate bitlink(if you enter in argument ussual link),or give you how much clicks was made on your bitlink(if you enter in argument bitlink)
### Arguments:
| Parameter|   Type   |                          Description                           |
| :------- | :------- | :------------------------------------------------------------- |
|  `Link`  | `string` | **Required**. Your Link,that you want to cut(Look Description) |

### How install it?

1.Install zip file with project

2.create .env file in folder with project

Tree of folder must look like this:

```
.env
requierements.txt
main.py
README.md
```

3.Open cmd

4. Open location with project

5. Enter command ```pip install -r requirements.txt.```
 
### How use it?

1.Open cmd

2.Open directory with Bitcut(Cd...)

3.Enter command ```Python main.py link```

P.S. **Link must be entered without quotation marks**

### Example of work

**Input:** ```Python main.py https://...```

**Output:** ```https://bit.ly/...```

### How create .env?
Create file and name it `.env`(it is name with file extension)

Open it in text redactor an write that:

`BITLY_TOKEN=TOKEN(Without quotation marks) `
