const lessons = [
    {
      question: "Qual a função do comando input() em Python?",
      options: [
        "A) Exibe uma mensagem de erro",
        "B) Mostra o tipo de dado",
        "C) Recebe dados do usuário pelo teclado"
      ],
      correct: 2
    },
    {
      question: "O que o código abaixo realiza?\n\nn1 = int(input(\"Digite um número:\"))\nn2 = int(input(\"Digite outro número:\"))\ns = n1 + n2\nprint(f'A soma entre n1 e n2 é {s}')",
      options: [
        "A) Compara os dois números e mostra o maior",
        "B) Soma dois números digitados e mostra o resultado",
        "C) Multiplica dois números digitados e mostra o resultado"
      ],
      correct: 1
    },
    {
      question: "O que o código abaixo analisa sobre a variável 'valor'?\n\nprint('o tipo primitivo desse valor é', type(valor))\nprint('Só tem espaços?', valor.isspace())\nprint('É um número?', valor.isnumeric())\nprint('É alfabeto?', valor.isalpha())\nprint('É alfanumérico', valor.isalnum())\nprint('Está em maiúsculas?', valor.isupper())\nprint('Está em minúsculas?', valor.islower())\nprint('Está capitalizado?', valor.istitle())",
      options: [
        "A) Executa operações matemáticas",
        "B) Converte a variável para maiúscula",
        "C) Verifica propriedades do conteúdo digitado"
      ],
      correct: 2
    },
    {
      question: "O que o código abaixo demonstra?\n\nn1 = int(input('Digite um número: '))\nn2 = int(input('Digite outro número: '))\n\ns = n1 + n2\nsub = n1 - n2\nm = n1 * n2\nd = n1 / n2\ne = n1 ** n2\nr = n1 % n2\n\nprint(f'A soma é: {s}\\nA subtração é: {sub}\\nA multiplicação é: {m}\\nA divisão é: {d:.2f}\\nA exponenciação é: {e}\\nO resto da divisão é: {r}')",
      options: [
        "A) Exibe somente o resultado da soma entre dois números",
        "B) Demonstra o uso de operadores aritméticos básicos em Python",
        "C) Cria uma função matemática personalizada"
      ],
      correct: 1
    },
    {
      question: "O que esse código exibe?\n\nn = int(input('Digite um número: '))\nprint(f'Analisando o valor: {n}, \\nO sucessor é: {n + 1},\\nO antecessor é: {n - 1}')",
      options: [
        "A) Mostra o quadrado do número digitado",
        "B) Mostra o dobro e a raiz do número digitado",
        "C) Mostra o antecessor e o sucessor de um número"
      ],
      correct: 2
    },
    {
      question: "O que esse código retorna?\n\nn = int(input('Digite um número: '))\nprint(f'O dobro de {n} vale {n*2}.\\nO triplo de {n} vale {n*3}.\\nA raiz quadrada de {n} vale {(n**(1/2)):.2f}.')",
      options: [
        "A) Mostra apenas a raiz cúbica de um número",
        "B) Mostra o dobro, o triplo e a raiz quadrada de um número",
        "C) Realiza apenas operações de subtração"
      ],
      correct: 1
    },
    {
      question: "O que esse código calcula?\n\nn1 = float(input('Primeira nota do aluno: '))\nn2 = float(input('Segunda nota do aluno: '))\nprint(f'A média entre {n1} e {n2} é igual a {(n1 + n2) / 2:.1f}.')",
      options: [
        "A) A soma das duas notas",
        "B) A diferença entre as notas",
        "C) A média aritmética das duas notas"
      ],
      correct: 2
    },
    {
      question: "O que esse código realiza?\n\nmedida = float(input('Uma distância em metros: '))\nkm = medida / 1000\nhm = medida / 100\ndam = medida / 10\ndm = medida * 10\ncm = medida * 100\nmm = medida * 1000\n\nprint(f'''\nA medida de {medida:.1f} m corresponde a:\n{km:.3f} km\n{hm:.3f} hm\n{dam:.3f} dam\n{dm:.0f} dm\n{cm:.0f} cm\n{mm:.0f} mm\n''')",
      options: [
        "A) Converte valores monetários",
        "B) Converte uma medida em metros para outras unidades",
        "C) Calcula apenas a metade de um número"
      ],
      correct: 1
    },
    {
      question: "Qual a saída do código abaixo?\n\nnum = int(input('Digite um número para ver sua tabuada: '))\nprint('-' * 12)\nprint(f'{num} x  1 = {num * 1}')\n...\nprint(f'{num} x 10 = {num * 10}')\nprint('-' * 12)",
      options: [
        "A) Mostra a tabuada de multiplicação de 1 a 10 para o número digitado",
        "B) Mostra a tabuada de adição",
        "C) Mostra apenas o dobro e triplo do número digitado"
      ],
      correct: 0
    },
    {
      question: "O que esse código faz?\n\nreal = float(input('Quanto você tem na carteira? R$ '))\ndolar = real / 5.78\neuro = real / 5.99\nprint(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')\nprint(f'Com R${real:.2f} você pode comprar €{euro:.2f}')",
      options: [
        "A) Converte reais em dólares e euros",
        "B) Converte reais em metros e centímetros",
        "C) Converte dólar para real"
      ],
      correct: 0
    },
    {
      question: "O que esse código realiza?\n\nlargura = float(input('Digite a largura da parede: '))\naltura = float(input('Digite a altura da parede: '))\narea = largura * altura\nprint(f'A sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')\ntinta = area / 2\nprint(f'Para pintar essa parede, você precisará de {tinta} litros de tinta.')",
      options: [
        "A) Calcula a área de uma parede e a quantidade de tinta necessária para pintá-la",
        "B) Converte metros em litros",
        "C) Soma a largura e a altura da parede"
      ],
      correct: 0
    },
    {
      question: "O que esse código realiza?\n\npreco = float(input('Qual é o preço do produto? R$'))\nnovo = preco - (preco * 5 / 100)\nprint(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}')",
      options: [
        "A) Aumenta o preço do produto em 5%",
        "B) Aplica um desconto de 5% no preço do produto",
        "C) Converte o preço do produto em dólar"
      ],
      correct: 1
    }
  ];
  
  function loadLesson(index, buttonElement) {
    const existing = buttonElement.parentElement.querySelector('.lesson-content');
    if (existing) {
      existing.remove();
      return;
    }
  
    document.querySelectorAll('.lesson-content').forEach(el => el.remove());
  
    const { question, options, correct } = lessons[index];
    const content = document.createElement('div');
    content.className = 'lesson-content';
  
    const questionEl = document.createElement('pre');
    questionEl.textContent = question;
    content.appendChild(questionEl);
  
    options.forEach((opt, i) => {
      const button = document.createElement('button');
      button.textContent = opt;
      button.className = 'option-button';
      button.onclick = () => {
        content.querySelectorAll('.option-button').forEach(btn => {
          btn.classList.remove('correct', 'incorrect');
          btn.disabled = true;
        });
        if (i === correct) {
          button.classList.add('correct');
        } else {
          button.classList.add('incorrect');
          content.querySelectorAll('.option-button')[correct].classList.add('correct');
        }
      };
      content.appendChild(button);
    });
  
    buttonElement.parentElement.appendChild(content);
  }  