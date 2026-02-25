Você deverá modificar o código Python em anexo () para utilizar uma URL de sua escolha (diferente de www.uefs.br).

Após realizar a alteração, execute o programa e elabore um documento em formato texto contendo:
A URL escolhida;
O valor retornado para o campo ;
O valor retornado para o campo ;
O valor retornado para o campo .

----------------------------------

### Anexo Get.py
```python
import requests
r = requests.get("http://www.uefs.br")
print(r.status_code)
print(r.headers)
print(r.content)
```
