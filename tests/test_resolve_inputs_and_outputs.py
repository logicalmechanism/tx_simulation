import pytest

from tx_simulation import resolve_inputs_and_outputs


@pytest.mark.parametrize("network", [True, False])
def test_resolve_inputs_and_outputs_invalid(network):
    # Replace 'valid_hex_cbor' with a valid hexadecimal string representing CBOR data
    valid_hex_cbor = '84A3008182582074686973206973206120737472696E6720696E73696465207468652063626F720001800200A0F5F6'
    with pytest.raises(KeyError) as excinfo:
        resolve_inputs_and_outputs(valid_hex_cbor, network)
    assert "required tx body elements are missing" in str(excinfo.value), "Incorrect error message for invalid hex"


def test_resolve_inputs_and_outputs_valid():
    # Replace 'valid_hex_cbor' with a valid hexadecimal string representing CBOR data
    valid_hex_cbor = '84a900828258200b5d93ee6482f42a2e5d21d8d5496b2e7e09dce787d4ed5401fed153af08d7b600825820589a17a9fba2c3fd4a4ef324ea7cc6d37b0d03314a25e04147f4f7dacc1a4f1b010d818258206e34390c14ea8041c85963cf4b00a4ac900ebfd4e7bbcc9df7ed9345393777f30012828258208f457077d56938420978dd2c47f1cf8cc0f5e0339b8e066b9c4ca63df086e15e01825820f60de32b7cf065e9f182d701078f0b310b965abdb5ca0cc24eb18dc4271c961d000182a200581d602d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc01821a00400ed4a2581c015d83f25700c83d708fbf8ad57783dc257b01a932ffceac9dcd0c3da14843757272656e63791a001e8480581c698a6ea0ca99f315034072af31eaac6ec11fe8558d3f48e9775aab9da14574445249501a000f4240a200581d602d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc011a76c2f34a10a200581d602d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc011a00932570111a00057110021a0003a0b50e82581c2d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc581cb834fb41c45bd80e5fd9d99119723637fe9d1e3fc467bc1c57ae9aee0b5820a25626d921a18ec23871bed8e6173d36cd73dbfae748fa96d7bf76f72e95b292a10581840000d87b80821a0006c5081a0a3a6c3df5f6'
    inputs, outputs = resolve_inputs_and_outputs(valid_hex_cbor, False)
    assert len(inputs) == len(outputs)


def test_resolve_inputs_and_outputs_wrong_network():
    # Replace 'valid_hex_cbor' with a valid hexadecimal string representing CBOR data
    valid_hex_cbor = '84a900828258200b5d93ee6482f42a2e5d21d8d5496b2e7e09dce787d4ed5401fed153af08d7b600825820589a17a9fba2c3fd4a4ef324ea7cc6d37b0d03314a25e04147f4f7dacc1a4f1b010d818258206e34390c14ea8041c85963cf4b00a4ac900ebfd4e7bbcc9df7ed9345393777f30012828258208f457077d56938420978dd2c47f1cf8cc0f5e0339b8e066b9c4ca63df086e15e01825820f60de32b7cf065e9f182d701078f0b310b965abdb5ca0cc24eb18dc4271c961d000182a200581d602d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc01821a00400ed4a2581c015d83f25700c83d708fbf8ad57783dc257b01a932ffceac9dcd0c3da14843757272656e63791a001e8480581c698a6ea0ca99f315034072af31eaac6ec11fe8558d3f48e9775aab9da14574445249501a000f4240a200581d602d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc011a76c2f34a10a200581d602d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc011a00932570111a00057110021a0003a0b50e82581c2d5fec7bbb8abbe1fb6590db2676389dffab196d212fb2b4b9902dcc581cb834fb41c45bd80e5fd9d99119723637fe9d1e3fc467bc1c57ae9aee0b5820a25626d921a18ec23871bed8e6173d36cd73dbfae748fa96d7bf76f72e95b292a10581840000d87b80821a0006c5081a0a3a6c3df5f6'
    inputs, outputs = resolve_inputs_and_outputs(valid_hex_cbor, True)
    assert len(inputs) == 5
    assert len(outputs) == 0


def test_resolve_inputs_and_outputs_inspect_input():
    valid_hex_cbor = '84a9008282582032e9634fcb724e26cb12d3f00e3c4f4eb4214caa5032f8f933f4e6c1f78fa0f3008258206681d3f753d56d425e39badc82a14e269454249ee4fed5f3fff0516f63416858020d818258206e34390c14ea8041c85963cf4b00a4ac900ebfd4e7bbcc9df7ed9345393777f30012828258205eb433065a423b53b465bb02430e1d3c6d4547fa1c2a4d82367d4e53df9bef5b01825820f60de32b7cf065e9f182d701078f0b310b965abdb5ca0cc24eb18dc4271c961d000182a200581d6039f29cfe6ab0765578a6e0d8871e1a3bc18f5d277b257095aabf1cd801821a0013669aa1581c92158340b4f3147aea48dd4bdb961878ec56f51f4cf4786a4490cf4ea15820000643b001e77f1930e631ee5dda454786a974ab69154cff0f71c9d0cb76f69501a200581d60e6f85717b932788e3b1e57b11e9f8bf190d257c57d369979c18a02dd011a080431e710a200581d60e6f85717b932788e3b1e57b11e9f8bf190d257c57d369979c18a02dd011a00935936111a00053d4a021a00037e310e82581cb834fb41c45bd80e5fd9d99119723637fe9d1e3fc467bc1c57ae9aee581ce6f85717b932788e3b1e57b11e9f8bf190d257c57d369979c18a02dd0b5820cd45e9822fcd789bc1e6c34192691241c0fc1a8b7c21be031542bd5be3846d7aa10581840000d87980821a00055c621a08177250f5f6'
    inputs, outputs = resolve_inputs_and_outputs(valid_hex_cbor, False)
    assert inputs[0][0] == '32e9634fcb724e26cb12d3f00e3c4f4eb4214caa5032f8f933f4e6c1f78fa0f3'
    assert len(inputs) == len(outputs)