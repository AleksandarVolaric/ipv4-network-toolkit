from main import main


# CLI analysis and return-to-menu behavior
def test_cli_analysis_returns_to_menu(monkeypatch, capsys):
    user_inputs = iter(["1", "192.168.10.34/27", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(user_inputs))

    main()

    output = capsys.readouterr().out
    assert "IPv4 address: 192.168.10.34" in output
    assert "Wildcard mask: 0.0.0.31" in output
    assert "Network address: 192.168.10.32" in output
    assert "IPv4 classification: Private" in output
    assert output.count("1. Analyze IPv4 network") == 2
    assert "Goodbye!" in output


def test_cli_invalid_cidr_returns_to_menu(monkeypatch, capsys):
    user_inputs = iter(["1", "192.168.10.999/27", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(user_inputs))

    main()

    output = capsys.readouterr().out
    assert "Invalid octet: 999." in output
    assert output.count("1. Analyze IPv4 network") == 2


def test_cli_conversion_returns_to_menu(monkeypatch, capsys):
    user_inputs = iter(["2", "192.168.10.34", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(user_inputs))

    main()

    output = capsys.readouterr().out
    assert "Binary address: 11000000.10101000.00001010.00100010" in output
    assert output.count("1. Analyze IPv4 network") == 2
    assert "Goodbye!" in output
