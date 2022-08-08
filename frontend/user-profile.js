
const togglePassword2 = document.querySelector('#tg1');
const password2 = document.querySelector('#password1');
  togglePassword2.addEventListener('click', function (e) {
    const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
    password2.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});


const togglePassword3 = document.querySelector('#tg2');
const password3 = document.querySelector('#password2');
  togglePassword3.addEventListener('click', function (e) {
    const type = password3.getAttribute('type') === 'password' ? 'text' : 'password';
    password3.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});


var characters="abcdefghijklmnopqrstuvwxyz"
var login=document.getElementById("btn1")
var form=document.getElementById("form")
var pass1=document.getElementById("password1")
var pass2=document.getElementById("password2")
var input=document.getElementsByTagName("input")
form.onsubmit=()=>{return false}

login.addEventListener("click",()=>{
 
        if(fname.value.length ==""){
            fname.classList.add("invalid")
            sp1.innerHTML="first name cannot be empty <img src='close-circle.svg' alt=''>"
        }
        

        if(lname.value ==""){
            lname.classList.add("invalid")
            sp2.innerHTML="last name cannot be empty <img src='close-circle.svg' alt=''>"
        }

        if(email.value ==""){
            email.classList.add("invalid")
            sp3.innerHTML="Email cannot be empty <img src='close-circle.svg' alt=''>"
        }

        if(username.value ==""){
            username.classList.add("invalid")
            sp4.innerHTML="Enter a valid username <img src='close-circle.svg' alt=''>"
        }

        if(pass1.value ==""){
            pass1.classList.add("invalid")
            sp6.innerHTML="password must be greater than six characters <img src='close-circle.svg' alt=''>"
        }

        if(pass2.value ==""){
            pass2.classList.add("invalid")
            sp5.innerHTML="confirm your pasword <img src='close-circle.svg' alt=''>"
        }

        if(pass2.value !== pass1.value){
            pass2.classList.add("invalid")
            sp5.innerHTML="password not match <img src='close-circle.svg' alt=''>"
        }
        

    
})

function log1(){
    if(fname.value.length <=2 || Number(fname.value)){
        fname.classList.add("invalid")
        sp1.innerHTML="<p>Wrong input</p> <img src='close-circle.svg' alt=''>"
    }else{
        fname.classList.add("valid")
        fname.classList.remove("invalid")
        sp1.innerHTML=""
        setTimeout(()=>{
            fname.classList.remove("valid")
        },2000)
    }

}

function log2(){
    if(lname.value.length <=2 || Number(lname.value)){
        lname.classList.add("invalid")
        sp2.innerHTML="<p>Wrong input</p> <img src='close-circle.svg' alt=''>"
    }else{
        lname.classList.add("valid")
        lname.classList.remove("invalid")
        sp2.innerHTML=""
        setTimeout(()=>{
            lname.classList.remove("valid")
        },2000)
    }

}

function log3(){
    if(email.value.length <=4 || Number(email.value)){
        email.classList.add("invalid")
        sp3.innerHTML="<p>Wrong input</p> <img src='close-circle.svg' alt=''>"
    }else{
        email.classList.add("valid")
        email.classList.remove("invalid")
        sp3.innerHTML=""
        setTimeout(()=>{
            email.classList.remove("valid")
        },2000)
    }

}

function log4(){
    if(username.value.length <=2 || Number(username.value)){
        username.classList.add("invalid")
        sp4.innerHTML="<p>Wrong input</p> <img src='close-circle.svg' alt=''>"
    }else{
        username.classList.add("valid")
        username.classList.remove("invalid")
        sp4.innerHTML=""
        setTimeout(()=>{
            username.classList.remove("valid")
        },2000)
    }

}

function log5(){
    if(pass2.value.length <=5){
        pass2.classList.add("invalid")
        sp5.innerHTML="<p>Password must match</p> <img src='close-circle.svg' alt=''>"
    }else{
        pass2.classList.add("valid")
        pass2.classList.remove("invalid")
        sp5.innerHTML=""
        setTimeout(()=>{
            pass2.classList.remove("valid")
        },2000)
    }
}

function log6(){
    if(pass1.value.length <=5){
        pass1.classList.add("invalid")
        sp6.innerHTML="<p>Password must be greater than six</p> <img src='close-circle.svg' alt=''>"
    }else{
        pass1.classList.add("valid")
        pass1.classList.remove("invalid")
        sp6.innerHTML=""
        setTimeout(()=>{
            pass1.classList.remove("valid")
        },2000)
    }

}