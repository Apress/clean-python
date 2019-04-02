# Example to show, how switch can be implimented, not working example.
def tanzania(amount):
    calculate_tax = <Tax Code>
    return calculate_tax

def zambia(amount):
    calculate_tax = <Tax Code>
    return calculate_tax

def eritrea(amount):
    calculate_tax = <Tax Code>
    return calculate_tax


contry_tax_calculate = {
	"tanzania": tanzania,
            "zambia": zambia,
   	"eritrea": eritrea,
}

def calculate_tax(country_name, amount):
    country_tax_calculate["contry_name"](amount)


calculate_tax("zambia", 8000000)
