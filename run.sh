curl --location --request GET 'https://api.printful.com/oauth/scopes' --header 'Authorization: Bearer amPFnWAkcjtgf8RZbbk7QLvJHaxfmgHapxtLGh43'

curl --location --request GET 'https://api.printful.com/products' --header 'Authorization: Bearer amPFnWAkcjtgf8RZbbk7QLvJHaxfmgHapxtLGh43'

# --header "X-PF-Store-Id: 10117137"

curl --location --request GET 'https://api.printful.com/store/products' --header 'Authorization: Bearer amPFnWAkcjtgf8RZbbk7QLvJHaxfmgHapxtLGh43' --header "X-PF-Store-Id: 10117137"