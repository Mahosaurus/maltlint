from src.maltes_formatter import MaltesFormatter

class TestFinalNewline:
    def test_final_newline(self):
        instance = MaltesFormatter("./tests/resources/test_final_newline/final_newline_missing.py")
        result = instance.run_test_mode()
        assert result.endswith("\n")
        assert not result.endswith("\n\n")

        instance = MaltesFormatter("./tests/resources/test_final_newline/final_newline_there.py")
        result = instance.run_test_mode()
        assert result.endswith("\n")
        assert not result.endswith("\n\n")
