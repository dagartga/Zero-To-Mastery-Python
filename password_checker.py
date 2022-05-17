import sys
import requests
import hashlib

def request_api_data(query_char):
    '''
        Takes in a SHA1 set of characters and returns
        a response of all the SHA1 matches from the website
        and the count of the number of times the password
        has been leaked.
        
        The response format is
            
            tail_sha1_characters:count
        
        Example for SHA1 five characters (A52BA):

            5CC7EDD3DF44AEB0B3B1A6232DC52445A2D:3362
    '''
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res



def get_password_leaks_count(hashes, hash_to_check):
    '''
        Takes in a string of the hashes:count from the API response and the tail of the SHA1 password.
        Splits the API response string by line and by hash value and count
        Returns the count if the hash value in the response equals the tail hash of the password to check.
        '''

    hashes = (line.split(':') for line in hashes.text.splitlines())

    for h, count in hashes:
        if hash_to_check == h:
            return count
    return 0
        



def pwnd_api_check(password):
    '''
        Takes in a password, converts it to SHA1 hash
        then to hexidecimal format and uppercase.
        The first five characters of the hexidecimal SHA1 hash
        are checked for matches on the website using the 
        request_api_data() function.
    '''

    if type(password) != str:
        password = str(password)
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char)
    print(tail)
    count = get_password_leaks_count(response, tail)

    return count





def main(args):
    for password in args:
        count = pwnd_api_check(password)
        if count:
            print(f'{password} was found to be leaked {count} times')
        else:
            print(f'Great password!! \nThe {password} has been leaked {count} times.')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
