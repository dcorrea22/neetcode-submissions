class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = ''
        for s in strs:
            prefix += str(len(s)) + '#'
        print(prefix + ''.join(strs))       
        return prefix + ''.join(strs)


    def decode(self, s: str) -> List[str]:
        breke = 0
        lista_numeros = []
        check_sum = 0
        tamanho_string = len(s)
        decoded_string = []
        
        for i in (range(tamanho_string)):
            if (s[i] == '#') and (check_sum <= (tamanho_string - i - 1)):                
                numeros = int(s[breke:i])
                lista_numeros.append(0 + numeros) 
                check_sum += numeros               
                breke = i + 1

            elif s[i].isdigit() == False:
                break

        for element in lista_numeros:
            decoded_string.append(s[breke:breke+element])
            breke += element 

        print(lista_numeros)         
        
        return decoded_string
