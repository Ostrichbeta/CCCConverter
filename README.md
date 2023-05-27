# CCCConverter

基於 [RIME-Cantonese](https://github.com/rime/rime-jyutping/blob/master/jyutping.dict.yaml) 及 [CCC](http://www.cuhk.edu.hk/ics/clrc/crcl_93_1/kataoka.pdf) 粵拼轉換表的[香港政府粵語拼音](https://zh.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E6%94%BF%E5%BA%9C%E7%B2%B5%E8%AA%9E%E6%8B%BC%E9%9F%B3)轉換器。

### 支援範圍
本程式的粵拼對照表來自 [RIME-Cantonese](https://github.com/rime/rime-jyutping/blob/master/jyutping.dict.yaml) 中收錄的單字，包括正體中文及常用的粵字共計 27087 字。簡化字可能需要先轉換成正體中文方可正常轉換，為了確保用字的準確，本程式將不會支援簡化字的粵拼轉換。

### 使用

轉換單句：使用`cccconverter.convert`中的`convert_sentence`方法可以將一句話的中文字轉換為對應的港府粵語拼法，如下：
```python
>>> convert_sentence("慈雲圩")
'tsz/tszi/tszu/tsi/tsee/chz/chzi/chzu/chi/chee wan/wun/wen hui||yu/yue||wai/wei'
```
因為 CCC 拼法中，同一個字，甚至是同一個音都有眾多的拼法，預設的情況下，轉換的結果會保留所有的拼法，其中，同一個音的不同的拼法會使用斜槓（/）相隔，不同音會用（||）相隔。

若僅需要寫出一個拼法，可以加上`only_keep_first_spell=True`引數：
```python
>>> convert_sentence("慈雲圩", only_keep_first_spell=True)
'tsz wan hui||yu||wai'
```

在上述基礎下，若僅需要一個讀音，可以再加上`only_keep_first_pronunciation=True`引數：
```python
>>> convert_sentence("慈雲圩", only_keep_first_spell=True, only_keep_first_pronunciation=True)
'tsz wan hui'
```

（兩個引數之間不衝突，可據實際情況組合使用）

若需要使生成結果作為列表顯示，可以使用`convert_sentence_map`函數，引數同上：
```python
>>> convert_sentence_map("慈雲圩")
[('慈', 'tsz/tszi/tszu/tsi/tsee/chz/chzi/chzu/chi/chee'), ('雲', 'wan/wun/wen'), ('圩', 'hui||yu/yue||wai/wei')]
```

If you have questions or better ideas about this package, please feel free to open an issue or request a PR!