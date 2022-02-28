create table crypto_tracking_platform
(
    ctp_name_id varchar(100) not null
        constraint pk_crypto_tracking_platform
            primary key,
    domain      varchar(100) not null,
    ip          varchar(9)   not null,
    root_https  varchar      not null
);

alter table crypto_tracking_platform
    owner to postgres;

create table price_tracking_platform
(
    ptp_name_id varchar(100) not null
        constraint pk_crypto_tracking_platform_0
            primary key,
    domain      varchar(100) not null,
    ip          varchar(9)   not null,
    root_https  varchar      not null
);

alter table price_tracking_platform
    owner to postgres;

create table raw_scraped_tokens
(
    token_id            varchar                                not null
        constraint pk_new_tokens_discovered
            primary key,
    ctp_name_id         varchar                                not null
        constraint fk_raw_scraped_tokens
            references crypto_tracking_platform,
    token_name          varchar(100)                           not null,
    discovery_timestamp timestamp(6) default CURRENT_TIMESTAMP not null,
    chain_name          varchar                                not null,
    listed_timestamp    timestamp(6) default CURRENT_TIMESTAMP not null,
    uri                 varchar
);

alter table raw_scraped_tokens
    owner to postgres;

create table scrapy_token
(
    listed_timestamp     timestamp(6) not null,
    discovered_timestamp timestamp(6) not null,
    ptp_name_id          varchar      not null
        constraint fk_ptp_name_id
            references price_tracking_platform,
    ctp_name_id          varchar      not null
        constraint fk_ctp_name_id
            references crypto_tracking_platform
);

alter table scrapy_token
    owner to postgres;

create table wallet
(
    net_worth      bigint default 0.0 not null,
    wallet_address varchar(34)        not null
        constraint pk_wallet
            primary key
);

alter table wallet
    owner to postgres;

create table chain
(
    chain_id   varchar(100) not null
        constraint pk_tbl
            primary key,
    chain_name varchar(100) not null,
    fk_coin_id varchar
);

alter table chain
    owner to postgres;

create table coin
(
    coin_id     varchar(100)     not null
        constraint pk_coin
            primary key,
    fk_chain_id varchar          not null
        constraint fk_chain_id
            references chain,
    coin_name   varchar(100)     not null,
    coin_price  double precision not null
);

alter table coin
    owner to postgres;

alter table chain
    add constraint fk_coin_id
        foreign key (fk_coin_id) references coin;

create table token
(
    token_contract     varchar(42)  not null
        constraint pk_token
            primary key,
    fk_chain_id        varchar      not null
        constraint fk_chain_id
            references chain,
    token_id           varchar(100) not null,
    total_suppy        bigint,
    market_cap         double precision,
    launched_timestamp timestamp(6),
    price_history      json         not null,
    token_name         varchar(100) not null,
    listed_timestamp   timestamp(6) not null
);

alter table token
    owner to postgres;

create table tracked_tokens
(
    token_contract varchar(42)                         not null
        constraint pk_tracked_tokens
            primary key
        constraint fk_token_contract
            references token,
    ptp_name_id    varchar                             not null
        constraint fk_price_tracking_platform_id
            references price_tracking_platform,
    tracked_since  timestamp default CURRENT_TIMESTAMP not null,
    last_updated   timestamp default CURRENT_TIMESTAMP not null
);

alter table tracked_tokens
    owner to postgres;

create table position_delivery
(
    order_id        integer          not null
        constraint pk_token_order
            primary key,
    wallet_address  varchar(100)     not null
        constraint fk_wallet_address
            references wallet,
    token_contract  varchar          not null
        constraint fk_token_contract
            references tracked_tokens,
    quantity_tokens double precision not null,
    timestamp       timestamp(6) default CURRENT_TIMESTAMP
);

alter table position_delivery
    owner to postgres;

create table active_positions
(
    order_id          integer not null
        constraint pk_active_orders
            primary key
        constraint fk_active_orders_token_order
            references position_delivery,
    actived_timestamp timestamp(6) default CURRENT_TIMESTAMP
);

alter table active_positions
    owner to postgres;

create table position_order
(
    order_id        integer      not null
        constraint pk_asset_order
            primary key
        constraint fk_order_id
            references position_delivery,
    wallet_address  varchar(100) not null
        constraint fk_wallet_address
            references wallet,
    order_timestamp timestamp(6) default CURRENT_TIMESTAMP
);

alter table position_order
    owner to postgres;

create table "position_status "
(
    order_id       integer                                    not null
        constraint fk_order_id
            references active_positions,
    current_profit double precision default 0.0               not null,
    last_update    timestamp        default CURRENT_TIMESTAMP not null,
    order_value    double precision default 0.0
);

alter table "position_status "
    owner to postgres;

create table transaction
(
    order_id         integer          not null
        constraint pk_tbl_4
            primary key
        constraint fk_order_id
            references position_delivery,
    wallet_address   varchar(100)     not null
        constraint fk_wallet_address
            references wallet,
    fees_cost        double precision not null,
    timestamp        timestamp(6) default CURRENT_TIMESTAMP,
    token_price      double precision,
    total_cost       double precision,
    transaction_type transaction_type not null
);

alter table transaction
    owner to postgres;

create table wallet_coins
(
    wallet_address varchar(44)                  not null
        constraint fk_wallet_address_0
            references wallet,
    coin_id        varchar(100)                 not null
        constraint fk_coin_id
            references coin,
    quantity       double precision default 0.0 not null
);

alter table wallet_coins
    owner to postgres;

create table wallet_tokens
(
    wallet_address varchar(44)                  not null
        constraint fk_wallet_address
            references wallet,
    token_contract varchar(100)                 not null
        constraint fk_token_contract
            references token,
    quantity       double precision default 0.0 not null
);

alter table wallet_tokens
    owner to postgres;

