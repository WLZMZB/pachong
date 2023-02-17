//window环境创建
const jsdom = require('jsdom')
const {JSDOM} = jsdom
const dom = new JSDOM('<!DOCTYPE html><p>hello</p>')
window = dom.window
 document = window.document
// const document = dom.window.document;
