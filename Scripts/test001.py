import pytest,allure

class Test_001:

    @allure.step(title='步骤说明001')
    @pytest.mark.parametrize("a",[1,2,3])
    def test_adc(self,a):
        allure.attach('描述','我是测试步骤001的描述')
        assert a!=2

    @allure.step(title='步骤说明002')
    @pytest.mark.parametrize("a",[2,3,4])
    def test_bcd(self,a):
        allure.attach('描述','我是测试步骤002的描述')
        assert a==2