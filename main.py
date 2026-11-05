
alunos = []
class Aluno:

    def __init__(self, matricula: int, nome: str, idade: int) -> None:
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def apresentar_aluno(self):
        return f"Matricula: {self.matricula} | Nome: {self.nome} | Idade: {self.idade}"

    def buscar_aluno_matricula(self):
        if matricula_aluno in any(alunos)
        


aluno1 = Aluno(109, "Subaru", 17)
aluno2 = Aluno(108, "Emilia", 108)
aluno3 = Aluno(107, "Beatrice", 400)
alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)

while True:

    print("\n--- GR_Alunos v0.2 ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair\n")

    opcao = input("O que deseja fazer? ")
    op = "s"
    if opcao == "1":
        while op == "s":
            print("\n__Cadastre um novo Aluno__" \
            "\n Adicione os dados do aluno abaixo:\n")
            matricula_aluno = int(input("Matirucula: "))
            nome_aluno = input("Nome: ")
            idade_aluno = int(input("Idade: "))
            for aluno in Aluno.matricula:
                if matricula_aluno in alunos :
                    print("Essa matricula já existe no banco de dados")
                    continue           
            
            else:
                alunos.append(Aluno(matricula_aluno, nome_aluno, idade_aluno))
            print("\n Aluno cadastrado")
            while True:
                s_n = input("Deseja continuar?(S/N)").lower()
                op = s_n
                if s_n == "s"  :
                    print("...")
                    break
                elif s_n == "n":
                    print("Saindo...")
                    break
                else: 
                    print("digite apenas S ou N")
                    continue
    elif opcao == "2":
        print("__Lista de Alunos__\n")
        for aluno in alunos:
            print(aluno.apresentar_aluno())
        input("\nPrecione enter para voltar ao menu: ")
    
    elif opcao == "3":
        print("Saindo...")
        break 
