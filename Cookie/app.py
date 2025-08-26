from flask import Flask, request, render_template, make_response

app = Flask(__name__)
FLAG = "byteme{y0u_4r3_1nd33d_w0rthy}"

@app.route('/')
def home():
    auth_cookie = request.cookies.get('auth')  

    if auth_cookie is None:  # If cookie is not set, set it to 'loki'
        resp = make_response(render_template('worthy_ctf_page.html'))
        resp.set_cookie('auth', 'bG9raQ==')  # 'loki' in Base64
        return resp
    
    if auth_cookie == "dGhvcg==":  # 'thor' in Base64
        return render_template('worthy_page_flag.html', flag=FLAG)
    else:
        return render_template('worthy_ctf_page.html')

if __name__ == '__main__':
    app.run(debug=True)