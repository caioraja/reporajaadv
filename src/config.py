import logging
import os


def log(dc):
    os.chdir("D:/Programas/reporajaadv")
    log_format = "%(asctime)s:%(levelname)s:%(filename)s:%(message)s"
    #log_format = "%(message)s"
    logging.basicConfig(
        filename=f"{dc['historia'][0]}.log",
        # w -> sobrescreve o arquivo a cada log
        # a -> não sobrescreve o arquivo
        filemode="w",
        level=logging.DEBUG,
        format=log_format,
        encoding="utf-8",
    )

    logger = logging.getLogger("root")
    for i in dc.keys():
        logger.info(f"{i}, {dc[i]}")
