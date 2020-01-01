package com.example.buildup.data;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

public class DesignInCategory {
    @SerializedName("DesignId")
    @Expose
    private Integer designId;
    @SerializedName("allImagesDesign")
    @Expose
    private List<AllImagesDesign> allImagesDesign = null;
    @SerializedName("allRAB")
    @Expose
    private List<AllRAB> allRAB = null;
    @SerializedName("CustomAtap")
    @Expose
    private List<CustomAtap> customAtap = null;
    @SerializedName("CustomPlafon")
    @Expose
    private List<CustomPlafon> customPlafon = null;
    @SerializedName("CustomLantai")
    @Expose
    private List<CustomLantai> customLantai = null;
    @SerializedName("CustomDinding")
    @Expose
    private List<CustomDinding> customDinding = null;
    @SerializedName("CustomCatDalam")
    @Expose
    private List<CustomCatDalam> customCatDalam = null;
    @SerializedName("CustomCatLuar")
    @Expose
    private List<CustomCatLuar> customCatLuar = null;
    @SerializedName("DesignName")
    @Expose
    private String designName;
    @SerializedName("DesignDesc")
    @Expose
    private String designDesc;
    @SerializedName("category")
    @Expose
    private Integer category;
    @SerializedName("creator")
    @Expose
    private Integer creator;

    public Integer getDesignId() {
        return designId;
    }

    public void setDesignId(Integer designId) {
        this.designId = designId;
    }

    public List<AllImagesDesign> getAllImagesDesign() {
        return allImagesDesign;
    }

    public void setAllImagesDesign(List<AllImagesDesign> allImagesDesign) {
        this.allImagesDesign = allImagesDesign;
    }

    public List<AllRAB> getAllRAB() {
        return allRAB;
    }

    public void setAllRAB(List<AllRAB> allRAB) {
        this.allRAB = allRAB;
    }

    public List<CustomAtap> getCustomAtap() {
        return customAtap;
    }

    public void setCustomAtap(List<CustomAtap> customAtap) {
        this.customAtap = customAtap;
    }

    public List<CustomPlafon> getCustomPlafon() {
        return customPlafon;
    }

    public void setCustomPlafon(List<CustomPlafon> customPlafon) {
        this.customPlafon = customPlafon;
    }

    public List<CustomLantai> getCustomLantai() {
        return customLantai;
    }

    public void setCustomLantai(List<CustomLantai> customLantai) {
        this.customLantai = customLantai;
    }

    public List<CustomDinding> getCustomDinding() {
        return customDinding;
    }

    public void setCustomDinding(List<CustomDinding> customDinding) {
        this.customDinding = customDinding;
    }

    public List<CustomCatDalam> getCustomCatDalam() {
        return customCatDalam;
    }

    public void setCustomCatDalam(List<CustomCatDalam> customCatDalam) {
        this.customCatDalam = customCatDalam;
    }

    public List<CustomCatLuar> getCustomCatLuar() {
        return customCatLuar;
    }

    public void setCustomCatLuar(List<CustomCatLuar> customCatLuar) {
        this.customCatLuar = customCatLuar;
    }

    public String getDesignName() {
        return designName;
    }

    public void setDesignName(String designName) {
        this.designName = designName;
    }

    public String getDesignDesc() {
        return designDesc;
    }

    public void setDesignDesc(String designDesc) {
        this.designDesc = designDesc;
    }

    public Integer getCategory() {
        return category;
    }

    public void setCategory(Integer category) {
        this.category = category;
    }

    public Integer getCreator() {
        return creator;
    }

    public void setCreator(Integer creator) {
        this.creator = creator;
    }
}
