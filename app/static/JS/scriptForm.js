const inputEmail = document.querySelector('#email');
const labelInputEmail = document.querySelector('.input-group__label');
const inputRadioAge = document.getElementsByName('age');
const inputsRange = document.querySelectorAll('.input-range');
const hoursValue = document.querySelectorAll('.h');
const submit = document.querySelector('.btn-submit');

const renderHours = ()=>{
    inputsRange.forEach(input=>{
        input.addEventListener('input',()=>{
            hoursValue.forEach(hour=>{
                if(input.classList.contains(hour.classList.item(1))){
                    hour.textContent = `${input.value} ${input.value==1 ? 'Hora': 'Horas'}`;
                    return;
                }
            });
        });
    });
}

inputEmail.addEventListener('blur',()=>{
    if(inputEmail.value!='') labelInputEmail.classList.add('label-top');
    else labelInputEmail.classList.remove('label-top');
});

renderHours();

document.querySelector('.close').addEventListener('click',()=>{
    document.querySelector('.message-container').classList.add('none');
});