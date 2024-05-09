# 考试结果批量发送

使用此程序以批量发送考试结果。

## 使用

准备好以下文件：
- `score.csv`：储存考试成绩，其包含的列包括姓名、学号、各小题得分、总分、位次。按照小题结构的不同，**需要修改 `process_student` 中的代码逻辑**。
- `students.json`：从 elearning 中抓包获取。

执行时，在环境变量中设置 `UIS_USERNAME` 和 `UIS_PASSWORD` 两项，并安装好相应浏览器的 webdriver。代码中使用 Safari 作为 webdriver，使用时需要修改以下部分。具体设置方式可以参考 Selenium 文档。

```python
driver = webdriver.Safari()
```