
class xpath():
    class coingecko():
        class recently_added():
            coin_name = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/a[@class='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between']/text()"
            coin_href = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/a[@class='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between']/@href"
            id = "//td[@class='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40']/div[@class='tw-flex']/div[@class='tw-flex-auto']/div[@class='tw-flex tw-items-center']/span[@class='tw-hidden d-lg-inline font-normal text-3xs ml-2']/text()"
            last_added = "//td[@class='trade p-0 col-market pl-2 text-center']/text()"
            
        class coin():
            contract = "//i/@data-address"
            chain = "//div[@class='tw-px-2.5 tw-flex tw-items-center tw-justify-center tw-py-1 tw-h-7 tw-my-0.5 tw-rounded-md  tw-text-sm tw-font-medium tw-bg-gray-100 tw-text-gray-800 dark:tw-text-white dark:tw-bg-opacity-10 hover:tw-bg-gray-200 dark:hover:tw-bg-opacity-20 tw-rounded-l-md']/span[@class='text-muted mr-2']/span/img/@src"
    
    class poocoin():
        class tokens():
            