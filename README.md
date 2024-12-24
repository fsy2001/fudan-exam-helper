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

### `students.json` 抓包步骤

1. 在 elearning 对应课程中进入“人员”页面。打开浏览器的开发人员工具，转到“网络”标签页。
2. 在“所有人员”下拉框中选择“学生”。在开发人员工具中寻找一条请求，类型为 `xhr`，预览的内容中包含数个学生的姓名等信息。复制其请求 URL，将其中的 `per_page` 参数更改为大于学生人数的数值。若其中有包含 `page` 参数，将其删除。
3. 在控制台用 `fetch` 函数发送更改后的请求。在网络中找到对应的请求，将其响应保存为 `students.json`。
