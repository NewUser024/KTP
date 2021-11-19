data_test_questions = {
        '1.' : 'Банк сплачує своїм вкладникам 8% річних. Визначте, скільки грошей треба покласти на рахунок, щоб через рік отримати 60 грн прибутку?',
        '2.' : 'Знайдіть координати точки М, відносно якої симетричні точки E(-3;8;7) і F(-9;6;1)',
        '3.' : 'Знайдіть натуральне, одноцифрове число N, якщо відомо, що сума 510 + N ділиться на 9 без остачі.',
        '4.' : 'У коробці є 80 цукерок, з яких 44 – з чорного шоколаду, а решта – з білого. Визначте ймовірність того, що навмання взята цукерка з коробки буде з білого шоколаду.',
        '5.' : 'Сторони трикутника, одна з яких на 8 см більша за другу, утворюють кут 120°, а довжина третьої сторони дорівнює 28 см. Знайдіть периметр трикутника.',
        '6.' : 'Свинцеву кулю радіуса 5 см переплавили в кульки однакового розміру, радіус кожної з яких – 1 см. Скільки таких кульок одержали? Втратами свинцю під час переплавлення знехтуйте.',
        '7.' : 'Знайдіть вектор с = 2a – b, Якщо a (3; – 1;2), b (-2; 2; 5).',
        '8.' : 'До складу української Премєр-ліги з футболу входять 16 команд. Упродовж сезону кожні дві команди грають між собою 2 матчі. Скільки всього матчів буде зіграно за сезон?',
        '9.' : 'Розвяжіть нерівність 10 - 3x > 4.',
        '10.' : 'Основою піраміди є ромб, гострий кут якого дорівнює 30°. Усі бічні грані піраміди на хилені до площини її основи під кутом 60°. Знайдіть площу бічної поверхні піраміди (у см?), якщо радіус кола, вписаного в її основу, дорівнює 3 см.',
        '11.' : 'Спростіть вираз а — |a|, якщо а < 0.',
        '12.' : 'Двоє робітників, працюючи разом, можуть скосити траву на ділянці за 2 години 6 хвилин. Скільки часу (у годинах) витратить на скошування трави на цій ділянці другий робітник, працюючи самостійно, якщо йому потрібно на виконання цього завдання на 4 години більше, ніж першому робітникові?',
        '13.' : 'Якщо m = n = 1, то 7— m =',
        '14.' : 'Точка С лежить на осіх прямокутної системи координат і знаходиться на відстані 5 від точки А(-2; 4). Відрізок АС перетинає вісь у. Знайдіть координати точки С.',
        '15.' : 'Відрізок AB перетинає площину а в точці О. Проекції відрізків AO і ВO на цю площину дорівнюють 5 см і 20 см відповідно. Знайдіть довжину відрізка АВ, якщо AO = 8 см.',
        '16.' : 'Діагональ рівнобічної трапеції є бісектрисою її гострого кута і ділить середню лінію трапеції на відрізки довжиною 13 см і 23 см. Обчисліть (у см^2) площу трапеції.',
        '17.' : 'Укажіть проміжок, якому належить корінь рівняння 0,5 (x — 4) = 1,5.',
        '18.' : 'У просторі задано пряму а і точку M, яка не належить цій прямій. Скільки всього прямих, що перетинають пряму а, можна провести перпендикулярно до неї через точку м?',
        '19.' : 'У прямокутній системі координат ху на площині задано рівнобедрений трикутник ABC, у якому AB ВС. Вершина В лежить на прямій у = 2х + 9. Визначте площу трикутника АВС, якщо А(-6; -8), C(4; -8).',
        '20.' : 'У кінотеатрі квиток на вечірній сеанс на 15 грн дорожчий за квиток на ранковий сеанс. Вартість чотирьох квитків на ранковий сеанс на 220 грн менша за вартість шістьох квитків на вечірній сеанс. Скільки гривень коштує один квиток на ранковий сеанс? Уважайте, що на кожному із сеансів квитки на всі місця коштують однаково.'
}
data_test_answers = {
        '1)' : '750',
        '2)' : '(-6;7;4)',
        '3)' : '3',
        '4)' : '0,45',
        '5)' : '60см',
        '6)' : '125',
        '7)' : '(8;-4;-1)',
        '8)' : '240',
        '9)' : '(-∞ ;2)',
        '10)' : '144',
        '11)' : '2a',
        '12)' : '7',
        '13)' : '8-n',
        '14)' : '(1;0)',
        '15)' : '40см',
        '16)' : '864',
        '17)' : '(4;8]',
        '18)' : 'Одну',
        '19)' : '75',
        '20)' : '65'

}

import PySimpleGUI as sg

sg.theme('Green')

col_test = [[ sg.Text(data_test_questions ['1.'])],
        [sg.Radio(data_test_answers ['1)'], "RADIO1", key = 'INPUT1', default=False), sg.Radio('700',"RADIO1", default = False), sg.Radio('725', "RADIO1", default = False), sg.Radio('5', "RADIO1", default = False)],
        [sg.Text(data_test_questions ['2.'])],
        [sg.Radio('(3;-5; 2)', "RADIO2", default = False), sg.Radio(data_test_answers['2)'], "RADIO2", key = 'INPUT2', default=False), sg.Radio('(0;7;2)', "RADIO2", default = False), sg.Radio('(-2;-5;7)', "RADIO2", default = False)],
        [sg.Text(data_test_questions ['3.'])],
        [sg.Radio('0', "RADIO3", default = False), sg.Radio('765', "RADIO3", default = False), sg.Radio('-7', "RADIO3", default = False), sg.Radio(data_test_answers ['3)'], "RADIO3", key = 'INPUT3', default=False)],
        [sg.Text(data_test_questions ['4.'])],
        [sg.Radio('45', "RADIO4", default = False), sg.Radio('0,4', "RADIO4", default = False), sg.Radio(data_test_answers['4)'], "RADIO4", key = 'INPUT4', default=False), sg.Radio('0', "RADIO4", default = False)],
        [sg.Text(data_test_questions ['5.'])],
        [sg.Radio('50см', "RADIO5", default = False), sg.Radio('0см', "RADIO5", default = False), sg.Radio(data_test_answers ['5)'], "RADIO5", key = 'INPUT5', default=False), sg.Radio('66см', "RADIO5", default = False)],
        [sg.Text(data_test_questions ['6.'])],
        [sg.Radio('100', "RADIO6", default = False), sg.Radio('120', "RADIO6", default = False), sg.Radio(data_test_answers['6)'], "RADIO6", key = 'INPUT6', default=False), sg.Radio('-31', "RADIO6", default = False)],
        [sg.Text(data_test_questions ['7.'])],
        [sg.Radio('(8;-2;0)', "RADIO7", default = False), sg.Radio(data_test_answers ['7)'], "RADIO7", key = 'INPUT7', default=False), sg.Radio('-4;2;10', "RADIO7", default = False), sg.Radio('(0;0;0)', "RADIO7", default = False)],
        [sg.Text(data_test_questions ['8.'])],
        [sg.Radio('230', "RADIO8", default = False), sg.Radio('0', "RADIO8", default = False), sg.Radio('400', "RADIO8", default = False), sg.Radio(data_test_answers['8)'], "RADIO8", key = 'INPUT8', default=False)],
        [sg.Text(data_test_questions ['9.'])],
        [sg.Radio(data_test_answers ['9)'], "RADIO9", key = 'INPUT9', default=False), sg.Radio('(0;2)', "RADIO9", default = False), sg.Radio('-99;-4', "RADIO9", default = False), sg.Radio('2;∞', "RADIO9", default = False)],
        [sg.Text(data_test_questions ['10.'])],
        [sg.Radio(data_test_answers['10)'], "RADIO10", key = 'INPUT10', default=False), sg.Radio('240', "RADIO10", default = False), sg.Radio('7', "RADIO10", default = False), sg.Radio('150', "RADIO10", default = False)],
        [sg.Text(data_test_questions ['11.'])],
        [sg.Radio('3a-5', "RADIO11", default = False), sg.Radio('a', "RADIO11", default = False), sg.Radio('-a', "RADIO11", default = False), sg.Radio(data_test_answers ['11)'], "RADIO11", key = 'INPUT11', default=False)],
        [sg.Text(data_test_questions ['12.'])],
        [sg.Radio('5', "RADIO12", default = False), sg.Radio(data_test_answers['12)'], "RADIO12", key = 'INPUT12', default=False), sg.Radio('0', "RADIO12", default = False), sg.Radio('144', "RADIO12", default = False)],
        [sg.Text(data_test_questions ['13.'])],
        [sg.Radio('5-3n', "RADIO13", default = False), sg.Radio('2n', "RADIO13", default = False), sg.Radio(data_test_answers ['13)'], "RADIO13", key = 'INPUT13', default=False), sg.Radio('-n', "RADIO13", default = False)],
        [sg.Text(data_test_questions ['14.'])],
        [sg.Radio(data_test_answers['14)'], "RADIO14", key = 'INPUT14', default=False), sg.Radio('(4;10)', "RADIO14", default = False), sg.Radio('7;21', "RADIO14", default = False), sg.Radio('-4;-2', "RADIO14", default = False)],
        [sg.Text(data_test_questions ['15.'])],
        [sg.Radio('55см', "RADIO15", default = False), sg.Radio(data_test_answers ['15)'], "RADIO15", key = 'INPUT15', default=False), sg.Radio('Інше', "RADIO15", default = False), sg.Radio('39см', "RADIO15", default = False)],
        [sg.Text(data_test_questions ['16.'])],
        [sg.Radio('865', "RADIO16", default = False), sg.Radio(data_test_answers['16)'], "RADIO16", key = 'INPUT16', default=False), sg.Radio('144', "RADIO16", default = False), sg.Radio('920', "RADIO16", default = False)],
        [sg.Text(data_test_questions ['17.'])],
        [sg.Radio('[7; 55]', "RADIO17", default = False), sg.Radio('(-11; 23)', "RADIO17", default = False), sg.Radio(data_test_answers ['17)'], "RADIO17", key = 'INPUT17', default=False), sg.Radio('(-31; -13)', "RADIO17", default = False)],
        [sg.Text(data_test_questions ['18.'])],
        [sg.Radio(data_test_answers['18)'], "RADIO18", key = 'INPUT18', default=False), sg.Radio('Чотири', "RADIO18", default = False), sg.Radio('Безліч', "RADIO18", default = False), sg.Radio('Дві', "RADIO18", default = False)],
        [sg.Text(data_test_questions ['19.'])],
        [sg.Radio('65', "RADIO19", default = False), sg.Radio(data_test_answers ['19)'], "RADIO19", key = 'INPUT19', default=False), sg.Radio('50', "RADIO19", default = False), sg.Radio('-75', "RADIO19", default = False)],
        [sg.Text(data_test_questions ['20.'])],
        [sg.Radio('75', "RADIO20", default = False), sg.Radio('35', "RADIO20", default = False), sg.Radio('20', "RADIO20", default = False), sg.Radio(data_test_answers['20)'], "RADIO20", key = 'INPUT20', default=False)],
        [sg.Button('Submit', size = (20, 3))]]
s = 0

layout = [[ sg.Column(col_test, scrollable=True, size = (1000, 950)) ]]

window_quiz = sg.Window('Quiz', layout, size = (1000,950))

while True:
        event, values = window_quiz.read()
        if event == sg.WIN_CLOSED:
                break
        if event == 'Submit':
                answers_boolean = [0]
                for i in range(1, 20):
                        answers_boolean.append (values['INPUT' + str(i)])
                s = sum(answers_boolean)
                print (s)
window_quiz.close()
