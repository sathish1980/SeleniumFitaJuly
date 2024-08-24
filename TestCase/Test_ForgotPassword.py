import pytest


class Test_ForgotPAssword:


    @pytest.mark.Sanity
    @pytest.mark.run(order=2)
    def test_fisttestcaseinFP(self):
        print(" First stest in FP")

    @pytest.mark.Sanity
    @pytest.mark.run(order=1)
    def test_secondestcaseinFP(self):
        print(" Second stest in FP")


