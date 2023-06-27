import requests
import hashlib
import sys

def request_api_data(query_param):
    url = "https://api.pwnedpasswords.com/range/" + str(query_param)
    result = requests.get(url) # review requests
    if result.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {result.status_code}, check an API and try again."
        )
    
    return result


def get_psw_leaks_count(hashes, hashes_to_check):
    hashes = (hash.split(":") for hash in hashes.splitlines())

    for hash, count in hashes:
        if hash == hashes_to_check:
            return count
        
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]

    response = request_api_data(first5_char)

    return get_psw_leaks_count(response.text, tail)
    

def main(passwords):
    for psw in passwords:
        count = pwned_api_check(psw)
        if count:
            print(f"{psw} was found {count} times ... you should change your password.")
        else:
            print(f"{psw} was not found. Good to go!")
    return "Success!"


if __name__ == "__main__":
    passwords = sys.argv[1:]
    main(passwords)
