from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename 
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cek_rekening'

app.config.from_pyfile('config.cfg')

ALLOWED_EXTENSION = set(['jpg'])
mysql = MySQL(app)


#pengecekan file degan menggunakan rsplit
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


def message(msg, sts):
	tasks = [
				{
					'message': msg,
					'status' : sts
				}
			]
	return  jsonify(tasks)

@app.route('/', methods=['GET', 'POST'])
def index():

	return render_template('index.html')

# rest_api tbl_laporan 

@app.route('/tbl_laporan_create', methods=['GET', 'POST'])
def tbl_laporan_create():
	if request.method == 'POST' and 'ids_laporan' in request.form:
 
		foto_ktp_pelapor 		= request.files['foto_ktp_pelapor']
		foto_bukti 				= request.files['foto_bukti']
 
		if foto_ktp_pelapor.filename != '' and foto_bukti.filename != '':
			details 				= request.form
			ids_kode				= details['ids_kode']
			no_rek					= details['no_rek']
			nama_rek_dilaporan		= details['nama_rek_dilaporan']
			no_rek_dilaporkan		= details['no_rek_dilaporkan']
			katagory_kasus			= details['katagory_kasus']
			jumlah_kerugian			= details['jumlah_kerugian']
			media_transaksi			= details['media_transaksi']
			detail_media_transaksi 	= details['detail_media_transaksi']	
			nama_pelapor			= details['nama_pelapor']
			no_tlp_pelapor			= details['no_tlp_pelapor']
			email_pelapor			= details['email_pelapor']
			no_ktp_pelapor			= details['no_ktp_pelapor']
			alamat_pelapor			= details['alamat_pelapor']
			kota_pelapor			= details['kota_pelapor']
			kronologi				= details['kronologi']
			tgl_transaksi			= details['tgl_transaksi']	
	
			foto_ktp_pelapor_name 	= '{}.jpg'.format(no_ktp_pelapor)
			foto_bukti_name 		= '{}.jpg'.format(no_ktp_pelapor)
			cur 					= mysql.connection.cursor()
			app.config['UPLOAD_FOLDER'] = 'images/laporan/foto_ktp_pelapor'
			foto_ktp_pelapor.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_ktp_pelapor_name)) 
			app.config['UPLOAD_FOLDER'] = 'images/laporan/foto_bukti'     
			foto_bukti.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_bukti_name))   
			sql 		= "INSERT INTO tbl_laporan(ids_kode, no_rek, nama_rek_dilaporan, no_rek_dilaporkan, katagory_kasus, jumlah_kerugian, media_transaksi, detail_media_transaksi, nama_pelapor, no_tlp_pelapor, email_pelapor, no_ktp_pelapor, alamat_pelapor, kota_pelapor, kronologi, tgl_transaksi, foto_ktp_pelapor, foto_bukti) VALUES ('{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}')".format(
            									   ids_kode, no_rek, nama_rek_dilaporan, no_rek_dilaporkan, katagory_kasus, jumlah_kerugian, media_transaksi, detail_media_transaksi, nama_pelapor, no_tlp_pelapor, email_pelapor, no_ktp_pelapor, alamat_pelapor, kota_pelapor, kronologi, tgl_transaksi, foto_ktp_pelapor_name, foto_bukti_name)
			cur.execute(sql)
			mysql.connection.commit()
			cur.close()
			return message('sukses upload data', True)

		else:
			return message('gagal upload data', False)

@app.route('/tbl_laporan_get', methods=['GET', 'POST'])
def tbl_laporan_get():
	if request.method == 'POST' and 'ids_laporan' in request.form:
		try:
			cur 					= mysql.connection.cursor()
			details 				= request.form
			ids_laporan				= details['ids_laporan']
			sql 					= "SELECT * from tbl_laporan where ids_laporan={}".format(ids_laporan)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				sql = "SELECT * from tbl_laporan where ids_laporan={}".format(ids_laporan)
				cur.execute(sql)
				r = [dict((cur.description[i][0], value)
						for i, value in enumerate(row)) for row in cur.fetchall()]

				return jsonify(r)

			else: 
				return message('data tidak ada', False)

		except:
			return message('data post tidak ada',False)
	else:
		cur = mysql.connection.cursor()
		cur.execute('''select * from tbl_laporan''')
		r = [dict((cur.description[i][0], value)
			for i, value in enumerate(row)) for row in cur.fetchall()]
    
		return jsonify(r)

@app.route('/tbl_laporan_put', methods=['GET', 'POST'])
def tbl_laporan_put():
	if request.method == 'POST' and 'ids_laporan' in request.form:
 
		foto_ktp_pelapor 		= request.files['foto_ktp_pelapor']
		foto_bukti 				= request.files['foto_bukti']
 
		if foto_ktp_pelapor.filename != '' and foto_bukti.filename != '':
			details 				= request.form
			ids_laporan				= details['ids_laporan']
			ids_kode				= details['ids_kode']
			no_rek					= details['no_rek']
			nama_rek_dilaporan		= details['nama_rek_dilaporan']
			no_rek_dilaporkan		= details['no_rek_dilaporkan']
			katagory_kasus			= details['katagory_kasus']
			jumlah_kerugian			= details['jumlah_kerugian']
			media_transaksi			= details['media_transaksi']
			detail_media_transaksi 	= details['detail_media_transaksi']	
			nama_pelapor			= details['nama_pelapor']
			no_tlp_pelapor			= details['no_tlp_pelapor']
			email_pelapor			= details['email_pelapor']
			no_ktp_pelapor			= details['no_ktp_pelapor']
			alamat_pelapor			= details['alamat_pelapor']
			kota_pelapor			= details['kota_pelapor']
			kronologi				= details['kronologi']
			tgl_transaksi			= details['tgl_transaksi']	
	
			foto_ktp_pelapor_name 	= '{}.jpg'.format(no_ktp_pelapor)
			foto_bukti_name 		= '{}.jpg'.format(no_ktp_pelapor)
			cur 					= mysql.connection.cursor()
			app.config['UPLOAD_FOLDER'] = 'images/laporan/foto_ktp_pelapor'
			foto_ktp_pelapor.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_ktp_pelapor_name)) 
			app.config['UPLOAD_FOLDER'] = 'images/laporan/foto_bukti'     
			# foto_bukti.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_bukti_name))   
			# sql 		= "UPDATE tbl_laporan SET (ids_kode, no_rek, nama_rek_dilaporan, no_rek_dilaporkan, katagory_kasus, jumlah_kerugian, media_transaksi, detail_media_transaksi, nama_pelapor, no_tlp_pelapor, email_pelapor, no_ktp_pelapor, alamat_pelapor, kota_pelapor, kronologi, tgl_transaksi, foto_ktp_pelapor, foto_bukti) VALUES ('{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}') where ids_laporan= 15".format(
   #          									   ids_kode, no_rek, nama_rek_dilaporan, no_rek_dilaporkan, katagory_kasus, jumlah_kerugian, media_transaksi, detail_media_transaksi, nama_pelapor, no_tlp_pelapor, email_pelapor, no_ktp_pelapor, alamat_pelapor, kota_pelapor, kronologi, tgl_transaksi, foto_ktp_pelapor_name, foto_bukti_name, ids_laporan)
			sql= "UPDATE `tbl_laporan` SET `ids_kode`='{}',`no_rek`='{}',`nama_rek_dilaporan`='{}',`no_rek_dilaporkan`='{}',`katagory_kasus`='{}',`jumlah_kerugian`='{}',`media_transaksi`='{}',`detail_media_transaksi`='{}',`nama_pelapor`='{}',`no_tlp_pelapor`='{}',`email_pelapor`='{}',`no_ktp_pelapor`='{}',`alamat_pelapor`='{}',`kota_pelapor`='{}',`kronologi`='{}',`tgl_transaksi`='{}',`foto_ktp_pelapor`='{}',`foto_bukti`='{}' WHERE {}".format(
											ids_kode, no_rek, nama_rek_dilaporan, no_rek_dilaporkan, katagory_kasus, jumlah_kerugian, media_transaksi, detail_media_transaksi, nama_pelapor, no_tlp_pelapor, email_pelapor, no_ktp_pelapor, alamat_pelapor, kota_pelapor, kronologi, tgl_transaksi, foto_ktp_pelapor_name, foto_bukti_name, ids_laporan)
			cur.execute(sql)
			mysql.connection.commit()
			cur.close()
			return message('sukses update data' ,True)

		else:
			return message('gagal update data', False)
	else:
		
		return message('bukan permintaan post', False)

@app.route('/tbl_laporan_delete', methods=['GET', 'POST'])
def tbl_laporan_delete():
	if request.method == 'POST' and 'ids_laporan' in request.form:
		try:
			cur 					= mysql.connection.cursor()
			details 				= request.form
			ids_laporan				= details['ids_laporan']
			sql 					= "SELECT * from tbl_laporan where ids_laporan={}".format(ids_laporan)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				sql = "DELETE FROM tbl_laporan WHERE ids_laporan={}".format(ids_laporan)
				cur.execute(sql)
				mysql.connection.commit()
				cur.close()
				return message('sukses delete data', True)

			else: 
				return message('data tidak ada', False)
		except:
			return message('data post tidak ada', False)

	else:
		return message('bukan permintaan post', False)




# rest_api tbl_user
@app.route('/tbl_user_login', methods=['GET', 'POST'])
def tbl_user_login():
	if request.method == 'POST' and 'no_ktp' in request.form and 'password' in request.form:
		try:
			cur 					= mysql.connection.cursor()
			details 				= request.form
			nik						= details['no_ktp']
			password				= details['password']
			sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}'".format(nik)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}' and password ='{}'".format(nik, password)
				cur.execute(sql)
				account 				= cur.fetchone()
				if account:
					sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}' and password ='{}'".format(nik, password)
					cur.execute(sql)
					r = [dict((cur.description[i][0], value)
							for i, value in enumerate(row)) for row in cur.fetchall()]

					return message(jsonify(r), True)
				else:
					return message('No KTP/Password salah', False)
			else: 
				return message('No KTP belum terdaftar', False)

		except Exception as err:
			return err
			# return message('data post tidak ada', False)
	else:
		cur = mysql.connection.cursor()
		cur.execute('''select * from tbl_user_rek''')
		r = [dict((cur.description[i][0], value)
			for i, value in enumerate(row)) for row in cur.fetchall()]
    
		return jsonify(r)


@app.route('/tbl_user_create', methods=['GET', 'POST'])
def tbl_user_create():
	if request.method == 'POST':
		details 				= request.form
		foto_pribadi			= request.files['foto_pribadi']
		foto_ktp				= request.files['foto_ktp']
		foto_tabungan			= request.files['foto_tabungan']
		foto_npwp				= request.files['foto_npwp']
		password				= details['password']
		ids_kode				= details['ids_kode']
		no_rek					= details['no_rek']
		nama_user				= details['nama_user']
		no_ktp					= details['no_ktp']
		no_tlp					= details['no_tlp']
		email					= details['email']
		nama_usaha 				= details['nama_usaha']	
		jenis_usaha				= details['jenis_usaha']
		alamat					= details['alamat']
		kota					= details['kota']
		try:
			cur 					= mysql.connection.cursor()
			details 				= request.form
			nik						= details['no_ktp']
			password				= details['password']
			sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}' and password ='{}'".format(nik, password)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				return message('data sudah ada', False)

			else: 
				if foto_pribadi.filename != '' and foto_ktp.filename != '' and foto_tabungan.filename != '' and foto_npwp.filename != '':

					foto_pribadi_name		= '{}.jpg'.format(no_ktp)
					foto_ktp_name			= '{}.jpg'.format(no_ktp)
					foto_tabungan_name		= '{}.jpg'.format(no_ktp)
					foto_npwp_name			= '{}.jpg'.format(no_ktp)

					cur 					= mysql.connection.cursor()

					app.config['UPLOAD_FOLDER'] = 'images/user/foto_pribadi'
					foto_pribadi.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_pribadi_name)) 

					app.config['UPLOAD_FOLDER'] = 'images/user/foto_ktp'   
					foto_ktp.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_ktp_name)) 

					app.config['UPLOAD_FOLDER'] = 'images/user/foto_tabungan'
					foto_tabungan.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_tabungan_name)) 

					app.config['UPLOAD_FOLDER'] = 'images/user/foto_npwp'   
					foto_npwp.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_npwp_name)) 

					sql 		= "INSERT INTO tbl_user_rek(ids_kode, no_rek, password, nama_user, no_ktp, no_tlp, email, nama_usaha, jenis_usaha, alamat, kota, foto_pribadi, foto_ktp, foto_tabungan, foto_npwp) VALUES ('{}','{}', '{}','{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}')".format(
		            										ids_kode, no_rek, password, nama_user, no_ktp, no_tlp, email, nama_usaha, jenis_usaha, alamat, kota, foto_pribadi_name, foto_ktp_name, foto_tabungan_name, foto_npwp_name)
					cur.execute(sql)
					mysql.connection.commit()
					cur.close()
					return message('sukses upload data', True)

				else:
					return message('gagal upload data', False)
		except:
			return message('data post tidak ada', False)

			
@app.route('/tbl_user_get', methods=['GET', 'POST'])
def tbl_user_get():
	if request.method == 'POST' and 'ids_user' in request.form:
		try:
			cur 					= mysql.connection.cursor()
			details 				= request.form
			ids_user				= details['ids_user']
			sql 					= "SELECT * from tbl_user_rek where ids_user={}".format(ids_user)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				sql = "SELECT * from tbl_user_rek where ids_user={}".format(ids_user)
				cur.execute(sql)
				r = [dict((cur.description[i][0], value)
						for i, value in enumerate(row)) for row in cur.fetchall()]

				return jsonify(r)

			else: 
				return message('data tidak ada', False)

		except:
			return message('data post tidak ada', True)
	else:
		cur = mysql.connection.cursor()
		cur.execute('''select * from tbl_user_rek''')
		r = [dict((cur.description[i][0], value)
			for i, value in enumerate(row)) for row in cur.fetchall()]
    
		return jsonify(r)

@app.route('/tbl_user_put', methods=['GET', 'POST'])
def tbl_user_put():
	if request.method == 'POST' and 'ids_user' in request.form:
 
		foto_pribadi			= request.files['foto_pribadi']
		foto_ktp				= request.files['foto_ktp']
		foto_tabungan			= request.files['foto_tabungan']
		foto_npwp				= request.files['foto_npwp']

		if foto_pribadi.filename != '' and foto_ktp.filename != '' and foto_tabungan.filename != '' and foto_npwp.filename != '':
			details 				= request.form
			ids_user				= details['ids_user']
			ids_kode				= details['ids_kode']
			no_rek					= details['no_rek']
			password				= details['password']
			nama_user				= details['nama_user']
			no_ktp					= details['no_ktp']
			no_tlp					= details['no_tlp']
			email					= details['email']
			nama_usaha 				= details['nama_usaha']	
			jenis_usaha				= details['jenis_usaha']
			alamat					= details['alamat']
			kota					= details['kota']

			foto_pribadi_name		= '{}.jpg'.format(no_ktp)
			foto_ktp_name			= '{}.jpg'.format(no_ktp)
			foto_tabungan_name		= '{}.jpg'.format(no_ktp)
			foto_npwp_name			= '{}.jpg'.format(no_ktp)

			cur 					= mysql.connection.cursor()

			app.config['UPLOAD_FOLDER'] = 'images/user/foto_pribadi'
			foto_pribadi.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_pribadi_name)) 

			app.config['UPLOAD_FOLDER'] = 'images/user/foto_ktp'   
			foto_ktp.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_ktp_name)) 

			app.config['UPLOAD_FOLDER'] = 'images/user/foto_tabungan'
			foto_tabungan.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_tabungan_name)) 

			app.config['UPLOAD_FOLDER'] = 'images/user/foto_npwp'   
			foto_npwp.save(os.path.join(app.config['UPLOAD_FOLDER'],  foto_npwp_name)) 

			sql 		= "UPDATE tbl_user_rek SET ids_kode = '{}', no_rek = '{}', password ='{}' nama_user = '{}', no_ktp = '{}', no_tlp = '{}', email = '{}', nama_usaha = '{}', jenis_usaha = '{}', alamat = '{}', kota = '{}', foto_pribadi = '{}', foto_ktp = '{}', foto_tabungan = '{}', foto_npwp ='{}' where ids_user = {}".format(
            									   ids_kode, no_rek, password, nama_user, no_ktp, no_tlp, email, nama_usaha, jenis_usaha, alamat, kota, foto_pribadi_name, foto_ktp_name, foto_tabungan_name, foto_npwp_name, ids_user)
			cur.execute(sql)
			mysql.connection.commit()
			cur.close()
			return message('sukses upload data', True)

		else:
			return message('gagal update data', False)
	else:
		
		return message('bukan permintaan post', False)

@app.route('/tbl_user_delete', methods=['GET', 'POST'])
def tbl_user_delete():
	if request.method == 'POST' and 'ids_user' in request.form:
		try:
			cur 					= mysql.connection.cursor()
			details 				= request.form
			ids_user				= details['ids_user']
			sql 					= "SELECT * from tbl_user_rek where ids_user={}".format(ids_user)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				sql = "DELETE FROM tbl_user_rek WHERE ids_user={}".format(ids_user)
				cur.execute(sql)
				mysql.connection.commit()
				cur.close()
				return message('sukses delete data', True)

			else: 
				return message('data tidak ada', False)
		except:
			return message('data post tidak ada', False)

	else:
		return message('bukan permintaan post', False)

mail = Mail(app)
s = URLSafeTimedSerializer('Thissasecret!')
@app.route('/confirm_login', methods=['GET', 'POST'])
def confirm_login():
	if request.method == 'POST':
		email 	 	 = request.form['email']
		password 	 = request.form['password']
		nik 	     = request.form['nik']
		nama 	 	 = request.form['nama']
		kode_bank 	 = request.form['kode_bank']
		try:
			cur 					= mysql.connection.cursor()
			sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}' ".format(nik)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				return message('User sudah terdaftar', False)
			else: 
				token 	 = s.dumps(email, salt='email-confirm')
				msg   	 = Message('Confirm-Email', sender='saputrapangestu98@gmail.com', recipients=[email])
				link  	 = url_for('confirm_login_token', token=token,nik=nik,kode_bank=kode_bank,nama=nama, password=password, _external=True)
				msg.body = 'Your link is {}'.format(link)
				mail.send(msg)
				return message('Link konfirmasi terkirim ke Email : {}'.format(email), True)
		# except OSError as err:
			# return message('terjadi kesalahan : {}'.format(err))
		except:
			return message('terjadi kesalahan', False)
	else:
		return message('bukan permintaan post', False)

@app.route('/confirm_login_token/<token>/<nik>/<kode_bank>/<nama>/<password>', methods=['GET', 'POST'])
def confirm_login_token(token, nik,kode_bank, nama, password ):
	try:
		email = s.loads(token, salt='email-confirm', max_age=233)
	except SignatureExpired:
		# return message('kode expired, Silahkan Sign Up kembali', False)
		return '<h2 style="color:red"><center>Kode expired, Silahkan Sign Up kembali.</center></h2>'
	
	if request.method == 'GET':
		details 				= request.form
		foto_pribadi			= ''
		foto_ktp				= ''
		foto_tabungan			= ''
		foto_npwp				= ''
		ids_kode				= kode_bank
		no_rek					= ''
		nama_user				= nama
		no_ktp					= nik
		no_tlp					= ''
		nama_usaha 				= ''
		jenis_usaha				= ''
		alamat					= ''
		kota					= ''
		status					= 'ACTIVE'
		try:
			cur 					= mysql.connection.cursor()

			sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}' ".format(no_ktp)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				return message('User sudah terdaftar', False)

			else: 
				sql 		= "INSERT INTO tbl_user_rek(ids_kode, no_rek, password, nama_user, no_ktp, no_tlp, email, nama_usaha, jenis_usaha, alamat, kota,status, foto_pribadi, foto_ktp, foto_tabungan, foto_npwp) VALUES ('{}','{}','{}', '{}','{}','{}','{}', '{}','{}','{}', '{}','{}','{}', '{}','{}','{}')".format(
		            										ids_kode, no_rek, password, 
		            										nama_user, no_ktp, no_tlp, email, nama_usaha, 
		            										jenis_usaha, alamat, kota,status, foto_pribadi, foto_ktp, 
		            										foto_tabungan, foto_npwp)
				cur.execute(sql)
				mysql.connection.commit()
				cur.close()
				# return '<h2 style="color:green">Sukses terdaftar, silahkan login.</h2>'
				return '<h2 style="color:green"><center>Sukses terdaftar, silahkan login.</center></h2>'

		# except OSError as err:
			# return message('terjadi kesalahan')
		except:
			return message('bukan permintaan post', False)
	else:
		return message('bukan permintaan get', False)


@app.route('/lupa_login', methods=['GET', 'POST'])
def lupa_login():
	if request.method == 'POST':

		nik 	     = request.form['nik']

		try:
			cur 					= mysql.connection.cursor()
			sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}' ".format(nik)
			cur.execute(sql)
			account 				= cur.fetchone()
			if account:
				sql 					= "SELECT * from tbl_user_rek where no_ktp ='{}'".format(nik)
				cur.execute(sql)
				r = [dict((cur.description[i][0], value)
						for i, value in enumerate(row)) for row in cur.fetchall()]
				for x in r:
					dt = x['email']
				# return message('{}'.format(dt), True)

				token 	 = s.dumps(dt, salt='email-lupa')
				msg   	 = Message('Lupa Password', sender='saputrapangestu98@gmail.com', recipients=[dt])
				link  	 = url_for('lupa_login_token', token=token, no_ktp=nik,_external=True)
				msg.body = 'Your link is {}'.format(link)
				mail.send(msg)
				return message('Link lupa password terkirim ke Email : {}'.format(dt), True)
			else:
				return message('User belum terdaftar', False)
		# except:
		except OSError as err:
			return message('terjadi kesalahan : {}'.format(err))
			# return message('terjadi kesalahan', False)
	else:
		return message('bukan permintaan post', False)
		# return render_template('mail.html')

@app.route('/lupa_login_token/<token>/<no_ktp>', methods=['GET', 'POST'])
def lupa_login_token(token, no_ktp):
	try:
		email = s.loads(token, salt='email-lupa', max_age=233)
	except SignatureExpired:
		# return message('kode expired, Silahkan Sign Up kembali', False)
		return '<h2 style="color:red"><center>Link expired, Silahkan Lupa Password kembali.</center></h2>'
	
	if request.method == 'GET':
		return render_template('form_password.html', nik=no_ktp)
		# return render_template('form_password.html')
	else:
		return message('bukan permintaan get', False)

@app.route('/lupa_password_login', methods=['GET','POST'])
def lupa_password_login():

	if request.method == 'POST':
		details 				= request.form
		password 				= details['password']
		confirm_password 		= details['confirm_password']
		nik 			 		= details['nik']
		cur 					= mysql.connection.cursor()
		sql 		= "UPDATE `tbl_user_rek` SET `password` = '{}' WHERE `tbl_user_rek`.`no_ktp` = {}".format(password,nik)
		cur.execute(sql)
		mysql.connection.commit()
		cur.close()
		return '<h2 style="color:green"><center>Sukses, password diperbarui, silahkan login.</center></h2>'
	else:
		return message('bukan permintaan post', False)
app.run(host='0.0.0.0',debug=True,)