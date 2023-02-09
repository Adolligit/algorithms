from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    'Chave com o tipo incorreto'
    with raises(TypeError):
        encrypt_message('Some message', '33')

    'Mensagem com o tipo incorreto'
    with raises(TypeError):
        encrypt_message(0, 33)

    'O valor é maior que o indice da mensagem'
    assert encrypt_message('excepcional', 15) == 'lanoicpecxe'

    'O valor é um número ímpar'
    assert encrypt_message('grandioso', 3) == 'arg_osoidn'

    'O valor recebido é um número par'
    assert encrypt_message('incrível', 4) == 'leví_rcni'
