

function cadastrar(){
    let SenhaUsuario= document.getElementById("senha").value
    let NomeUsuario= document.getElementById("usuario").value
    if (SenhaUsuario =! null ){
        alert ('Sua senha é: ' + SenhaUsuario + ' seu usuário é: ' + NomeUsuario)
    }
    else{ 
        alert ('não funcionou')
    }
    
}

