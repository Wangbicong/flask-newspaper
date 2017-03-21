from requests import get, post

HOST = 'http://localhost:5000/api'


def post_reader():
    print post(HOST+'/reader', json={
        'wechat_key': 'ewafaew1313',
        'phone_number': '18800463845'
    })


if __name__ == '__main__':
    post_reader()