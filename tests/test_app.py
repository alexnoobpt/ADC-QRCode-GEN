from src.app import main


def test_main_runs(capsys):
    main()
    assert "qrcodegen" in capsys.readouterr().out
