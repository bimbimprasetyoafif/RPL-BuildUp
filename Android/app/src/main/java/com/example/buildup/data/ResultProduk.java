package com.example.buildup.data;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

public class ResultProduk {

    @SerializedName("ProductId")
    @Expose
    private Integer productId;
    @SerializedName("allImagesProduct")
    @Expose
    private List<AllImagesProduct> allImagesProduct = null;
    @SerializedName("ProductName")
    @Expose
    private String productName;
    @SerializedName("ProductDesc")
    @Expose
    private String productDesc;
    @SerializedName("ProductPrice")
    @Expose
    private Integer productPrice;
    @SerializedName("ProductStock")
    @Expose
    private Integer productStock;
    @SerializedName("ProductSatuan")
    @Expose
    private Integer productSatuan;
    @SerializedName("ProductNamaSatuan")
    @Expose
    private String productNamaSatuan;
    @SerializedName("ProductCategory")
    @Expose
    private Integer productCategory;
    @SerializedName("creator")
    @Expose
    private Integer creator;

    public ResultProduk(String productName, Integer productPrice) {
        this.productName = productName;
        this.productPrice = productPrice;
    }

    public Integer getProductId() {
        return productId;
    }

    public void setProductId(Integer productId) {
        this.productId = productId;
    }

    public List<AllImagesProduct> getAllImagesProduct() {
        return allImagesProduct;
    }

    public void setAllImagesProduct(List<AllImagesProduct> allImagesProduct) {
        this.allImagesProduct = allImagesProduct;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public String getProductDesc() {
        return productDesc;
    }

    public void setProductDesc(String productDesc) {
        this.productDesc = productDesc;
    }

    public Integer getProductPrice() {
        return productPrice;
    }

    public void setProductPrice(Integer productPrice) {
        this.productPrice = productPrice;
    }

    public Integer getProductStock() {
        return productStock;
    }

    public void setProductStock(Integer productStock) {
        this.productStock = productStock;
    }

    public Integer getProductSatuan() {
        return productSatuan;
    }

    public void setProductSatuan(Integer productSatuan) {
        this.productSatuan = productSatuan;
    }

    public String getProductNamaSatuan() {
        return productNamaSatuan;
    }

    public void setProductNamaSatuan(String productNamaSatuan) {
        this.productNamaSatuan = productNamaSatuan;
    }

    public Integer getProductCategory() {
        return productCategory;
    }

    public void setProductCategory(Integer productCategory) {
        this.productCategory = productCategory;
    }

    public Integer getCreator() {
        return creator;
    }

    public void setCreator(Integer creator) {
        this.creator = creator;
    }
}
