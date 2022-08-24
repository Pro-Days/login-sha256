import hashlib

def main_command_notlogin():
	print("\n회원가입: 1\n로그인: 2\n프로그램 종료: 3")

	command = str(input("\n명령: "))

	if command == '1':
		register()
	elif command == '2':
		login()
	elif command == '3':
		exit()
	else:
		print("\n올바르지 않은 입력입니다.")
		main_command_notlogin()

def main_command_logined():
	global logining_id
	print(f"\n\n로그인 아이디: {logining_id}\n\n로그아웃: 1\n프로그램 종료: 2")

	command = str(input("\n명령: "))

	if command == '1':
		logout()
	elif command =='2':
		exit()
	else:
		print("\n올바르지 않은 입력입니다.")
		main_command_logined()

def register():
	global register_id
	register_id = str(input("\n회원가입\n\n아이디: "))
	if register_id != '':
		global register_password1
		register_password1 = str(input("비밀번호: "))
		register_password2 = str(input("비밀번호 확인: "))

		f = open("id_and_password.txt", 'r')
		lines = f.readlines()
		for line in lines:
			line = str(line.strip().split(" ")[0])

			if register_id == line:
				print("\n해당 아이디는 이미 가입되었습니다.")
				main_command_notlogin()
				break
		f.close()

		if register_password1 == register_password2 and len(register_password1) > 6:
			store_id_and_password()
			print("\n회원가입 완료")
			main_command_notlogin()
		elif register_password1 == register_password2 and len(register_password1) < 7:
			print("\n비밀번호가 너무 짧습니다.")
			main_command_notlogin()
		else:
			print("\n비밀번호가 일치하지 않습니다.")
			main_command_notlogin()
			pass

def store_id_and_password():
	global register_password1

	global password
	password = register_password1

	store()
	global store_password

	global register_id

	data = register_id + ' ' + store_password + '\n'

	f = open("id_and_password.txt", 'a')
	f.write(data)
	f.close()

def login():
	login_id = str(input("\n로그인\n\n아이디: "))
	login_password = str(input("비밀번호: "))

	global password
	password = login_password

	store()
	global store_password

	f = open("id_and_password.txt", 'r')
	lines = f.readlines()
	for line in lines:
		id_line = str(line.strip().split(" ")[0])
		password_line = str(line.strip().split(" ")[1])

		if login_id == id_line and store_password == password_line:
			print("\n로그인 성공")
			global logining_id
			logining_id = login_id
			f.close()
			main_command_logined()
			break
		else:
			pass
	print("\n로그인 실패")
	main_command_notlogin()
	
def store():
	global password
	global store_password
	store_password = hashlib.sha256(bytes.fromhex(password)).digest().hex()

def logout():
	global logining_id
	logining_id = ''
	main_command_notlogin()

main_command_notlogin()