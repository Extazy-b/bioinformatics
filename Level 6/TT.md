**Задание**

*Итак, вы научились проводить филогенетический анализ как белок-кодирующих, так и некодирующих генов, освоили несколько программ и алгоритмов и умеете создавать простые скрипты для автоматизации анализа. И теперь настало время перейти на следующий уровень. В этом задании вам предстоит проанализировать генетическое разнообразие коронавируса SARS-CoV-2, гуляющего нынче по планете. Набор инструментов останется почти тем же, разве что опять придётся поменять программу для парного выравнивания. На этот раз предложу вам использовать отвергнутый нами ранее из-за своей низкой чувствительности при поиске гомологичных последовательностей BLASTn. BLASTn один из наиболее простых инструментов для парного выравниваня, он идеален, когда вы сравниваете схожие последовательности, и намного быстрее и проще использованного ранее HMMER. Филогению вируса можно строить как по всему геному, но это долго и требует вычислительных ресурсов, так и по отдельным его генам. Самый мейнстримный ген SARS-CoV-2 — тот, что кодирует S-белок, который торчит на поверхности вируса. Помните? Если нет, то Google saves. Ну или на обложку задания посмотрите что ли. Но почему ген Ы-белка такой популярный? Все дело в том, что именно он связывается с рецепторами ACEII на поверхности наших клеток, то есть мутации в нём будут напрямую влять на прочность взаимодействия вируса с клеткой и, следовательно, на его поведение. Поэтому предлагаю вам его и использовать в этом задании. Хотите взять какой-то другой белочек? Why not?*

**Ход работы**
1. Выбрать регион мира или смириться с назначенным.

1. Перейти на сайт [www.gisaid.org](https://www.gisaid.org/), войти под своей учётной записью и скачать все полные геномы коронавируса, выявленные в выбранном регионе.

1. Сохранить выбранные геномные последовательности в тексовом файле с расширением .fasta.

1. Скачать последовательность гена S-белка (или любого иного) вот [отсюда](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2?from=21563&to=25384&report=fasta). А сам референчный геном SARS-CoV-2 можно посмотреть вот тут.

1. Сохранить полученные последовательности в формате .fasta.

1. Найти в скачанных геномах выбранный ген. Для этого нужно, используя последовательность выбранного гена в качестве запроса и файл с геномными последовательностями в качестве базы, провести выравнивание. Это можно сделать и в десктопной, и в web-версии BLASTn.

1. Скачать результаты выравнивания в .fasta файл, выбрав "Aligned sequences". Этот файл будет содержать последовательности выбрнного Вами гена со всеми их мутациями.

1. Теперь из заголовков в скачанном файле нужно убрать все символы кроме букв "A-Z", цифр "0-9", знака ">" в начале заголовка и underscore (_ -- подчёркивание). Неподходящие симолы можно заменить на underscore. Это нужно потому, что Mr.Bayes не воспринимает любые другие символы. Также длина заголовка не должна превышать 99 символов.

1. Теперь множно перевести нуклеотидные последовательности гена в аминокислотные, сделав in silico трансляцию на этом [сайте](https://www.bioinformatics.org/sms2/translate.html).

1. Запустить множественное выравнивание в [MAFFT](https://mafft.cbrc.jp/alignment/software/) с использованием алгоритма [E-INS-i](https://mafft.cbrc.jp/alignment/software/algorithms/algorithms.html). Можно запускать выравнивание, как и в предыдущей задаче, а можно прописать в командной строке все параметры разом: mafft --genafpair --maxiterate 1000 input_file > output_file

1. Результат множественного выравнивания можно посмотреть в программе [Jalview](http://www.jalview.org/getdown/release/#). Она кросплатформенная и очень простая. Правда, посмотрите, чтобы понять, как оно хотя бы выглядит.

1. Сконвертировать полученный .fasta файл в формат .nexus в [web-конвертере](http://phylogeny.lirmm.fr/phylo_cgi/data_converter.cgi) или в [seqmagick](https://fhcrc.github.io/seqmagick/). При использовании seqmagick seqmagick convert --output-format nexus --alphabet dna YOUR_FILE.fasta YOUR_FILE.nexus

1. Провести реконструкцию филогенетического дерева в Mr.Bayes по параметрам, описанным ниже.

1. Открыть сгенерированное дерево в редакторе [FigTree](http://tree.bio.ed.ac.uk/software/figtree/) или [Interactive Tree of Life](https://itol.embl.de/) на ваш выбор, выбрав файл с расширением .con.tre.

1. Проанализировать дерево, его биологическую корректность.

1. Сделать вывод о генетическом разнообразии коронавируса.

1. Отредактировать дерево, выбрав шрифт и кегль, покрасив клады в разные цвета, повесить на него что-нибудь.

1. Mission comleted! You're breathtaking!

[Список регионов](https://www.google.ru/maps)

Запуск mafft
```
В консоли ввести mafft --genafpair --maxiterate 1000 input_file > output_file
--genafpair — ключ, который запускает выравнивание по алгоритму E-INS-i
--maxiterate 1000 — а этот ключ указывает число генераций отдельных выравниваний, можно оставить 1000, можно больше, можно меньше
input_file — файл с ортологами
output_file — название файла, куда программа будет выводить результат множественного выравнивания