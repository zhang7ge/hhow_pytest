from common.http_methods import common_request
import pytest
import json
import logging

api_url = "https://www.httpbin.org"
methods = common_request(api_url)

def test_get_methods():
    result = methods.get("/get")
    assert result.status_code == 200, "状态码非200，接口测试失败"

def test_post_methods():
    data = "hhow test post methods"
    json_data = json.dumps(data)
    result = methods.post("/post", json=json_data)
    assert result.status_code == 200, "状态码非200，接口测试失败"
    assert "hhow test post methods" in result.json()["data"], "data数据写入错误"

def test_put_methods():
    data = "hhow test put methods"
    json_data = json.dumps(data)
    result = methods.put("/put", json=json_data)
    assert result.status_code == 200, "状态码非200，接口测试失败"
    assert "hhow test put methods" in result.json()["data"], "data数据写入错误"

def test_delete_methods():
    params = "data"
    result = methods.delete("/delete", params = params)
    assert result.status_code == 200, "状态码非200，接口测试失败"
    assert result.json()["data"] == "", "data数据删除错误"

def test_patch_methods():
    data = "hhow test patch methods"
    json_data = json.dumps(data)
    result = methods.patch("/patch", json=json_data)
    assert result.status_code == 200, "状态码非200，接口测试失败"
    assert "hhow test patch methods" in result.json()["data"], "data数据写入错误"