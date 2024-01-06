def code_secret(message):
    """Renvoie le code secret caché dans la liste de chaînes"""
    code_total = 1  # Initialisez à 1 pour pouvoir multiplier
    for mau in message:
        premier_chiffre, dernier_chiffre = None, None  # Initialisez à None
        for i in range(len(mau)):
            if mau[i].isdigit():
                if premier_chiffre is None:
                    premier_chiffre = mau[i]
                dernier_chiffre = mau[i]

        if premier_chiffre is not None and dernier_chiffre is not None:
            code_total *= int(premier_chiffre + dernier_chiffre)

    return code_total


message_2 = ["AerE4vcL5Dfgf9Yv", "ShjhgJ5kHdVjhBsdfK"]
attendu_2 = 2695

message_30 = [
    "kRfBlDgMEXBccujMYFCXDvituUxG4XjNyNuoHrfYWQxvhXSYtOcc",
    "CpIuXjxMiQqHxUMoDrJUhZISWfM3lFVVNwEFE3ZGtZjVrsM",
    "HvPSUN4QHHJKil9L8qIk5HqgmDQYu3BiG9MHakZ6b",
    "LinCvOFgNeYcOmzd4DWaG12Jxozg1A1ilHpAwAVPEZaUKvzmWZQth73HM",
    "uyyzVJSV2p6PtLLPwWbXb5FRggfALSPT4CTznopDvvXMFmrrQXRu8pc3FlFm",
    "QbnYctLwOsCLD18chdDaEOlpYCDsJCncxnxffJMmEjsIdy",
    "uWeY8bRi1VHqUMrWVtMjcm8WbP46pKjs9vbgNEvb3MiMEtZTu9u",
    "svUo9C7PaI6IYRjqJDgWvZ3oZ3uSOqZgog3qXFmSHV7UpgaS",
    "FpunnrduLWhQA4fwXoRvm81KdwLOujVvOtZFgkQIPPjYpxkl2yJ",
    "MCGHEdLdmHrnZ6Og7fFrefLG5FXnHS2nnvIliGJJbE14CMiMf4RyK",
    "SZf6VJKASFGAEMblYJdGQYnwudo6VyAdHq3UWPmD64QdoCQlGWYCzEhWfw",
    "YmiXutKl1nxHbKTDYF9towhqUXD8zkYxQxepmns99xAkrlRxIslIEj",
    "3hDCrK7lq1UpXI68eosKDM1klJlQ7NOSKPXtXyz1ix5dH6Mvla",
    "CvxpAxWU8lAKZmewwuLuZBoaZnAT1VZxCrWgDBIuhlANvRBVpNBHZX",
    "OGXoKcfBVPzYnw6QJdsOkfMLrpWsBZePL9CT5LmJI58M",
    "yhNbkjdj6rPIPXNEFALtrcoftibEHnbTHbHSEoWxytVeREVYc",
    "zgsHnWqzwgS5ZBltoTOFJBYYkGTkQEURt6Di1jki8SeLU6AM2S",
    "mT6rDUe1U3seVVyuOIJIjBZ4IIjAOtEKG5cJyd7kpa2jAt",
    "etsfZdAcg5SBJOktaFfTMUrxfOkyTvsGtjBCRG3uFcA2SdZAMKHf5fOiDZl",
    "4RRuh1jnFad9VZi2tZxLoVWVn2282H3y9dFuVHLkCCwQR",
    "2zmsneFyjbabXPZyIXC5uM4W1yB17fx8wIPEwzFzNdMYpK",
    "4F9vPSIifpCJVFako7qaTHZqOdoN2x3a9c4LXKIND2sT",
    "t7yQQtcrwBD2LvWhCcxZjBmGpy1GsUFbhUrJDZMLsFYaZ",
    "C7fS3Mc4pWMhsaIOrDHG1zHd54dD8DwRZh8jAEZK81RL",
    "qMSUgSRJkk9cBCWumvUSvOBeMl6tvYMnUo879kTZlwESXRXDwIAD",
    "4imwUaLVWjpHgHzCXAuNcToYlhRgylOu4kzrQYfcpT",
    "rpqPcYyNNGRGgNnEraVkwnAnpUX8YjPI5YrlgFwGIxG",
    "jtWl632CRQdwxSZCRbFwIC12HbBj7ZxfN8KCMqIvTiy2MqliKw3eIX",
    "DSW3ZGBTydywFhIuxdXG2SGGgCWhRWimXtGg9Prw3LBVxTgvQbWuewVVSIji",
    "NeIJRQWN4BARRoXgyiFGXWLMJ5nrkmGEmctsCkQCsZwfjIF",
]

attendu_30 = 783447347670693474780953104229788749567331663872000

message_100 = [
    "OF1ANt5jHbVRk4zMbVmrFtgOWwEt94MaDHylDHXsH",
    "E7oXFanhLZTzvC5OBKlh2MvObOMdLHIeIHrsiRryyLoZloIbnGf2Xr",
    "bkuzAGGiOQbKfbyTusJqNCjlOMrCQvXuiqDOQQivcUC5HkPbIebjkje",
    "8LzaX7aFMryk8cF1EbIk4vjDr4vQcFCpNMOCfmbotG39LadJbXYAPGXkYz",
    "N3QgwaGfm6HQzsbBahClGK9jTKVdeBWZkssBdv4iTTJmk8cYvdNk",
    "FxEtvAJqCihsirAdKxg2ByamCod2r76O2MplGbBfIIhViXnjBC6qf",
    "DrTpmOHOVUH9ORxavGHrRtjbGLTpvZOpLpWrGiJHuRfnaVfoTZ5R",
    "PnLMPa7hRloyEvZkrWZNbBRvaQEO5JTpXct5aBGUdBpgsVQAAtDdAon4IBR",
    "nhH4BtHlFFwR9Zuy3xuU11i9MuTlimsZBd7zRGCTkKYiGb",
    "MoZYKFzToBMPqNrxOP4EzIyJWlImLryV2c1KuiofgNMyjvrFgYtycFfPQz",
    "ah1xsEsgbCMSZPcINezUfSjGnPECejuOUcqBHxNeOowZvl",
    "TWwOyqQVmRDjwy92RxycwciKNttJHJZfWobUMmKmDv",
    "dPkp7MT7lvptHShLfwa2jomr4ESqBarVZ9Q5AJwKgnmCRaZmTs",
    "ytY6FsbbxBNBr36EbtITtyBBMrIfAaJMeRBdHqePK5jScaQXmZ",
    "jemPhsUzkJGBcxQRliBf9iZKhmvfWbWLjMTHQCPfuQsllIvJRBvI",
    "htTwXBX7iSJsGOMp18NRHrbQ9lfVl6BFTNStRGpCzIDE7ASkA5fX",
    "M7MQcEiPOZO79cphW6Voex4mhlUSp1A43Wk9f2mNALbEDURJVG",
    "g9kg37figAN3rDY5TDcyeZuLfUKzMoNQKVxkrnkIUHSFaE34b",
    "HIgSyDzHTvvWErV5D1KB6ZCosjm9CJwRRlNKxYBv3xc729VRFtVCgt",
    "ik4WkdqGsNXAOVJKIPaoVcZRFtCHRrJGOWMOycWfpyD7ij5OgRRNwdLud3K",
    "Sv3Z8KtU8sEvdLukPh7pLgstIorUp3dotfPKRxpu37VcyTHVIEO",
    "DYoTiBibYsShIYXBrIp4CBOiFkimZWPGyqVRoMJUDoWWO4fdbiMCLJCfTu",
    "LsESj3Orab6A6CIAksPUHLHNrP5l1K55ZSNTHGHe",
    "BYGUTdnPaivDMpbZ5aoDtaPcO4hxr6IDFtNBT8EVLtcRIeC",
    "iZDrEIrQ5cH5qOmnxHP8ANsVjUjo1WGxkwqZrt4Eul9PspsSqoQC",
    "Ijh8nPAjNBhimtXfCgME6zX7rtYwkYim6fBILa3pM8P1OcgwewDi3I",
    "zv2LYIIsyxdxRE1tFkOeveO5KlVih93fan7TsNBx",
    "XPPNXqOCQHintFBvNXEeQxXlCyK1DlFNIsnSRfuLPyCIcpDaqEfnre",
    "8aPq2qgFntU77rLVdqyS4iBYHXS8Ez9hKNYIJACgoC",
    "zRiSOSdeov1mW49eyJwa3TKkZBDGogQynPzzTaNP5sC",
    "IPl7IvRCffOhFXPxwiQZ4tVqPr5Jc2sXzpu5GHZHIfxj",
    "9RDajybhb8eHnAMCWIfyWCP8iOYUI2F44LZl2dbfAn",
    "YcubMEruEjzWjiYoomdTtSJNoUneQMfw3DTrG7KjUiA6nlZByDKTotRxbnb",
    "N5vnahhN5YN6HTLtprxqrZ1YbFtpMakrXcDxjtTkdYCqpQhFlJI",
    "JuUfz8eLmw3mgWVFXw7CUytIvSMOm55xRIeVgIagbD3MGTqKDnDqtRo197j",
    "vFrGoEcltWKmjkdpSAOFaFqzStvsnvJldnXI7qRgpNmQGkcMjNLliZ",
    "lQ2WfAIfwfnJwbevPKply5hPc1OQ6llHwjEEGppovJCb7mW4eSfC3RK",
    "AFNY2ssFegACHJW9UMeYBLluGG28CFZY4dBASOjwtXOlLjWvv",
    "HT4Zp7iJh3uUbz5CeCpbDXr59ZjgtptIYhkvSknIBEIzv",
    "Xg7InFDMDDiyaFQOjlMekHxiKOSQlSMDGTZI1mos",
    "SR6H1ofwUGw1YSn4cXmvrlvwltwnkyWDt3cxVcjzJCzfNckIdIWvFZfS",
    "XNnUUixfAeqInmZjJRXWZiPZBGYZf7XCnPLjYTgixjSFy8t",
    "qOs4IAw54ohgxrjjmfPNd4NwAoe5YcO5IyBiqH984bk",
    "6rQyWLysHRR3zjL9zqyxiZfN4sxPVpxDyCeb1muJ59PcH9BueNEiG",
    "C1lYDbdhy4y73Cno9gGf1NgXg6yWKcrk4lY19GhldEwrZ",
    "CxcLRlCrWr1zHLcmKTf4dQQgTIxp32n39ffZIY7KYQfqnKmqQ6XtiY",
    "dAqHx9SKfoDWe8dgTjNNzZ8RVWpFScEL7hmMsh9a4fVu47rLWVzjM3dGj",
    "XlTVvbUWUsKQUht9vsuSxrDnlj7E5glpv5Es1nbEh4vT63HOZY",
    "WMMGQAST9uTMum9FofVgVnOce9XrEW9taDFPq9zpRXoKIHHM9s",
    "eVLBdHKW6TLYxduAnIVEbkECeTHgZ6NZEYJbvurzyegkpByHtEabvQerDP",
    "COC2VwSWKZQSf5aW23I9nG6EzVDcv6dhCSJz928JCBULyDe",
    "EvQh6qonY7XVwvcIzVvAFUIcG4MRyDpOr1meX3QGUyoWB",
    "OTMljFf3ALOFMS9ctsnEuVCCYAILAQhpOkqscdwOGdRYj9yrm",
    "1ksaGTvXaSxQKleFeiGTYEk9VVJPyVynzi5au2AmFAPp7XYSVKNPws8PcNp",
    "e8bRGqS3hrMwz5NP2bExTy7HP74GPYX4MB3AyNplO1gLSB",
    "HUnKhzfxGvTvE3V6cvumIZx3z7B9M5fuzhFtRVGU",
    "eVZHjAmeOLgQXNVmnQWCqMqBZ5fw4cyWFiX5spaUaTFzqpxL5bcFRMAY",
    "PHXguUA3J6QgGYeuArWsmaxq1eaLyY58YB9c34ifhVisXkqf",
    "sTQDeGwGMRj8AgUF8Zg9sxnwkaHHixF6foQL9KXy44LA8eb7viU4Gh",
    "qEfQT4CZyS2sqgk3A8bCzlUQcMS8DioqNGD3DlFRiJV",
    "JBe1XfbdcGw8sadSfzkDmiWsaQEagyrfXFD4aheHpdr",
    "dMn8RsGeK6uv9CcXqo3GH6Y1zXUaRerXFGavgdLkq4Z4slgrBy",
    "UgzHcRonp7eYCGO6PYkWc7K1GPvqhYzOsvnBtSUpKKGwdDqAJcU",
    "CNRHKWeaVfb8CDAoCh4eQjiHXydA1mDkl5XVpBaR",
    "J7zJRfAbFYdVEH5NNjhve3NxCiUO6LZfCDbJzXjz",
    "nhN1XQtDmj3nuIo5zGKrjLoFqiuYMPmBkVrAlVTfroDSskVjqwDohGBfFaX",
    "ubjwRkYWzdHbcgyyfY2srrw52ReFl5VOJCuRXBw8YnkaozI",
    "tJlSALLnwAu67NCZZSP7Yf3lzzJW6HXvSofG1rNL",
    "FZxqXeZk2EyRDAmZGxphNH8aXf2rIOmmHZlX5ReDXolkQOsHG",
    "8yEzzsCozJbWnZJE8rUSx46oiymnXEsfY6AjIpkv",
    "YAkJ1yIfgMhhCMCDGKa1pZJfnmCIvxtVxJjd4wcz9OLqeTVWTzt5rEf",
    "owzggM7mqN3emHpCHmavnUqIdHcBDOeYPFKVUBP3ekE2VP4jtZNVFSvmbeAn",
    "8pcGXb7pmrcxNBP4PF5ZOuy935Xh8TGg8FjcaFQjxNXlr",
    "3KLMWqJ7pr4Pw4kZ9A8Bzl1jTVhIZJ3yFU7EW7sMiZyLpD",
    "8ww8LcukO8i5zUrYKTIGN53lHBvMO6ARWyX3M71M",
    "UGDPrTsxNsVOtClVZo5Hk2GwP6jGmNxCyF3i9ABYiuliRLriGYlXIHaH",
    "KjUyaGdnbKSfXRaknkQpLKPCPSxZZgx9HCyPUW4bRyKSdAEMVqjyuoz9L",
    "7YUIrBYB5le8qbeents8kAJaKrFsJmqRQlPCoFVPRIxoDaALY4Xa",
    "ijTCmoxEXdWDnKBtXFdOAqK6JWlX66FdxNfFSECm3qyi",
    "rlUO9n34VFfppFSHDTL7bLz9vj3T44Tz1nbtCxMnsM4AAfJNPK",
    "Nbs4IbFJ51ecykR4SCTTHVTCtpeaZcrnFFxxXznlP1FSYnATFLwbcbvMV",
    "J5dGdgIwCk5HCppWiz4oWjDCZMSQ5fgo8DnUaazXsCHC",
    "AP9xww9MNn7GSTCnjaqusWOY7uGUdlGsQaHoUx36R",
    "fmvLhrRizwocQBJlbTYkMcVYXy4tlYMEBFnNjINpucayoNPNEr",
    "rGu8HZB6JYomvgQPC3WGnqhDHgUajFWVOJgekONgHcuVGmMxH",
    "KhfuQWbNugdeFNBjiHtVeYejgEUwnhCt5OwIpAoNPCeAKBacM",
    "vIzvCW7926rP2z7GsHEvpVoOKBh6eKUGpKXqO57ME",
    "JIJoRmDDnrVITBvzqcVvRzDLIlxBTyv6EVwVxwttjuiCjbuh",
    "COJcWHp5ET6AqoVCtUWpjav97xqofB7JG7HktKtU9QAG7R",
    "RlF1Nw3NGApHtiKhgD6ekM5JZsZuz2FQ6wZJ6HaxRxTyyi3jcGg1o5cERNqj",
    "3oNYik2PrHxrSjFEAhtXMFf3eb6RWjzQfnGLxUx9gMTYhdy4XIzG5x",
    "CjxXEItMPGSTuMFujEy23RiHJrhv6YH9iHUbvBeLiB83fqO",
    "GlqWUJ6xDC5mz9MTkdnMJ9xhDxxaTuJOaklCN4bgXjAj",
    "ry7Hbbz2CnHpvaihLbSiMyzrkNnGnYwIwiYr6VcFA7xktCSyijPmJLd",
    "n5x9uOXWODAmkpIyWuWtNfuXSSFL5frUxqTqKB1JVol",
    "hN4UAwn7ULVMr71mL1RrrDdgChj7pZOjQpHG4hlWVRW2kYr2HWayuDMBGB",
    "7MFoWLfJdZbl2WAIjsKezBleN1GjxrEOCz5KX6MGth6Pu8ec",
    "gt6t4SgkAfQyjZpBdoVbQZsDzrWknLkYkRELCdnPROnx",
    "Ht3DVVI76lDvXdSkP6EjBKpSHwyd52WBkYWK2TaxCT3ve5xaW1rEXXzgcCv",
    "gi3s6AnZMnOT3W5CrcpjvUdn3CTRvw9QH9kCxUDJR1UdgvuczYneave5rjt",
]

attendu_100 = 53898904587274718630367566672935867319452849983159001495811716286362942841060299725718479962155879647236329234880093035540355891316692154557587783680000000000000000000000


assert code_secret(message_2) == attendu_2
assert code_secret(message_30) == attendu_30
assert code_secret(message_100) == attendu_100
