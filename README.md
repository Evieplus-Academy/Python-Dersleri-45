# Python Dersleri 44 - REGEX


### Python Regex Özet Tablo (Cheat Sheet)

| Özellik / Desen      | Açıklama                                                                    | Örnek                  |
|----------------------|-----------------------------------------------------------------------------|------------------------|
| `.`                  | Herhangi bir karakterle eşleşir (yeni satır hariç)                          | `a.c` -> "abc", "a+c"  |
| `\d`                 | Rakamla eşleşir (0-9)                                                       | `\d\d` -> "12", "56"   |
| `\D`                 | Rakam olmayan karakterle eşleşir                                            | `\D\D` -> "ab", "+%"   |
| `\w`                 | Harf, rakam veya alt çizgiyle eşleşir                                       | `\w\w` -> "a5", "A_"   |
| `\W`                 | Harf, rakam veya alt çizgi olmayan karakterle eşleşir                       | `\W\W` -> "@!", "&%"   |
| `\s`                 | Boşluk karakteriyle eşleşir (boşluk, sekme, yeni satır vb.)                | `\s\w` -> " a", "\t1"  |
| `\S`                 | Boşluk karakteri olmayanla eşleşir                                          | `\S\s` -> "a ", "1\t"  |
| `[abc]`              | Köşeli parantezler içindeki karakterlerden herhangi biriyle eşleşir         | `a[123]` -> "a1", "a3" |
| `[^abc]`             | Köşeli parantezler içindeki karakterler dışındakilerle eşleşir              | `a[^123]` -> "ab", "a_"|
| `^`                  | Metnin başıyla eşleşir                                                       | `^abc` -> "abc..."     |
| `$`                  | Metnin sonuyla eşleşir                                                       | `abc$` -> "...abc"     |
| `*`                  | Önceki karakterin sıfır veya daha fazla tekrarıyla eşleşir                  | `ab*c` -> "ac", "abc", "abbc" |
| `+`                  | Önceki karakterin bir veya daha fazla tekrarıyla eşleşir                    | `ab+c` -> "abc", "abbc"|
| `?`                  | Önceki karakterin sıfır veya bir kez tekrarıyla eşleşir                     | `ab?c` -> "ac", "abc"  |
| `{m,n}`              | Önceki karakterin en az m ve en fazla n kez tekrarıyla eşleşir              | `a{2,4}` -> "aa", "aaa", "aaaa" |
| `()`                 | Gruplama için kullanılır, içindeki desenleri bir grup olarak işler          | `(ab)+` -> "ab", "abab"|
| `\|`                 | Alternatif desenleri belirtir, `\|` ile ayrılan desenlerden herhangi biriyle eşleşir | `a|b` -> "a", "b" |
