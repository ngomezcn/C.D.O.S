
class xpath():
    class recently_added():
        coin_name = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/a[@class='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between']/text()"
        coin_href = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/a[@class='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between']/@href"
        id = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/span[@class='tw-hidden d-lg-inline font-normal text-3xs ml-2']/text()"

    class coin():
        network = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/a[@class='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between']/text()"
