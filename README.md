# Exercise 1

* Prompt: What are the most common special characters used in Python regular expressions?
![Common Special Characters in RegEx](images/CommonRegExSpecial.png)

* Prompt: Write a Python regular expression that matches a 10-digit phone number with hyphens.
![10 Digit Phone RegEx](images/RegEx10DigitPhone.png)

* Write a Python regular expression that matches a street address with a number and a street name, followed by ST or AVE.
![Street Address RegEx](images/StreetAddressRegex.png)

* Write a Python regular expression that matches a full name with any common title like Mr or Mrs followed by any number of names beginning with capital letters, possibly with hyphens between some names.
```python
import re

pattern = r"(Mr|Mrs|Ms|Dr|Prof)\.?\s+[A-Z][a-zA-Z]*(?:-[A-Z][a-zA-Z]*)*(?:\s+[A-Z][a-zA-Z]*(?:-[A-Z][a-zA-Z]*)*)*"
```
![Name Prefix RegEx](images/NamePrefixRegEx.png)

* Write a regular expression that matches any legal URL.
```python
import re

pattern = r"((http|https|ftp)://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[\w\-._~:/?#[\]@!$&'()*+,;=]*)?"
```
![RegEx to match Legal URLs](images/URLRegEx.png)

* What is a raw string in Python?
![Raw String Response](images/RawStringResponse.png)